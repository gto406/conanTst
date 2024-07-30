#include <vector>
#include <string>
#include <iostream>

#include <nlohmann/json.hpp>

using json = nlohmann::json;

int main() {
	json myJSObj;

	std::vector<std::string> vec;
	vec.push_back("test_package");
	vec.push_back("nlohmann_json");

	myJSObj["foo"] = vec;
	
	// Output value...
	std::cout << myJSObj << "\n";
}
