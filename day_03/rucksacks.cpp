#include <iostream>
#include <string>
#include <fstream>
#include <set>
#include <vector>
#include <numeric>

int get_priority(char c)
{
    if (c >= 'a' && c <= 'z')
        return c - 'a' + 1;

    if (c >= 'A' && c <= 'Z')
        return c - 'A' + 27;

    return 0;
}

int total_priority(const std::set<char>& chars)
{
    std::vector<int> priorities;
    priorities.reserve(chars.size());

    std::transform(chars.begin(), chars.end(), std::back_inserter(priorities), get_priority);
    int result = std::accumulate(priorities.begin(), priorities.end(), 0);
 
    return result;
}

template <typename T>
std::set<T> vec_to_set(const std::vector<T>& v)
{
    return {v.begin(), v.end()};
}

template <typename Container>
std::set<char> find_common(const Container& first, const Container& second)
{
    std::vector<char> common;
    std::set_intersection(first.begin(), first.end(), second.begin(), second.end(), std::back_inserter(common));

    return std::set<char>{common.begin(), common.end()};
}

struct Rucksack
{
    std::vector<char> first;
    std::vector<char> second;
    std::vector<char> all;

    static Rucksack from_string(const std::string& s)
    {
        assert(s.size() % 2 == 0);

        const size_t half_size = s.size() / 2;
        Rucksack rucksack{};
        rucksack.first = std::vector<char>{s.begin(), s.begin() + half_size};
        rucksack.second = std::vector<char>{s.begin() + half_size, s.end()};
        rucksack.all = std::vector<char>{s.begin(), s.end()};

        std::sort(rucksack.first.begin(), rucksack.first.end());
        std::sort(rucksack.second.begin(), rucksack.second.end());
        std::sort(rucksack.all.begin(), rucksack.all.end());

        return rucksack;
    }
};

std::optional<int> sum_up_priorities(const std::string& fname)
{
    std::ifstream in{fname};
    std::string line;

    if (!in.is_open())
        return std::nullopt;

    int result = 0;
    while (std::getline(in, line)) {
        auto r = Rucksack::from_string(line);
        result += total_priority(find_common(r.first, r.second));
    }

    return result;
}

char find_common_char_in_multiple_rucksacks(const std::vector<Rucksack>& rucksacks)
{
    size_t n_chars_total = 0;
    for (const auto& r : rucksacks) {
        n_chars_total += r.all.size();
    }

    std::vector<char> all_chars;
    all_chars.reserve(n_chars_total);

    for (const auto& r : rucksacks) {
        all_chars.insert(all_chars.end(), r.all.begin(), r.all.end());
    }

    auto all_chars_set = vec_to_set(all_chars);

    for (const auto& r : rucksacks) {
        auto s = vec_to_set(r.all);
        all_chars_set = find_common(all_chars_set, s);
    }

    return *all_chars_set.begin();

}

std::optional<int> summarize_groups_of_three(const std::string& fname)
{
    std::ifstream in{fname};
    std::string line;

    if (!in.is_open())
        return std::nullopt;

    int counter = 0;
    int result = 0;
    std::vector<Rucksack> group;
    while (std::getline(in, line)) {
        auto r = Rucksack::from_string(line);
        group.push_back(r);
        ++counter;

        if (counter == 3) {
            char common_char = find_common_char_in_multiple_rucksacks(group);
            result += get_priority(common_char);

            counter = 0;
            group = {};
            continue;
        }
    }

    return result;
}

int main()
{
    assert(157 == sum_up_priorities("data/test_input.txt").value());
    assert(70 == summarize_groups_of_three("data/test_input.txt").value());

    std::cout << "Sum of priorities: " << sum_up_priorities("data/input.txt").value() << "\n";
    std::cout << "Sum of priorities (groups of 3): " << summarize_groups_of_three("data/input.txt").value() << "\n";
}