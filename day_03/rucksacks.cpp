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

struct Rucksack
{
    std::vector<char> first;
    std::vector<char> second;

    static Rucksack from_string(const std::string& s)
    {
        assert(s.size() % 2 == 0);

        const size_t half_size = s.size() / 2;
        Rucksack rucksack{};
        rucksack.first = std::vector<char>{s.begin(), s.begin() + half_size};
        rucksack.second = std::vector<char>{s.begin() + half_size, s.end()};

        std::sort(rucksack.first.begin(), rucksack.first.end());
        std::sort(rucksack.second.begin(), rucksack.second.end());

        return rucksack;
    }

    std::set<char> find_common() const
    {
        std::vector<char> common;
        std::set_intersection(first.begin(), first.end(), second.begin(), second.end(), std::back_inserter(common));

        return std::set<char>{common.begin(), common.end()};
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
        result += total_priority(r.find_common());
    }

    return result;
}

int main()
{
    assert(157 == sum_up_priorities("data/test_input.txt").value());

    std::cout << "Sum of priorities: " << sum_up_priorities("data/input.txt").value() << "\n";
}