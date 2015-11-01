#include <iostream>
#include <string.h>
#include "Leap.h"

using namespace Leap;

int main(int argc, char** argv) {
    SampleListener listener;
    Controller controller;

    controller.addListener(listener);

    // Keep this process running until Enter is pressed
    std::cout << "Press Enter to quit..." << std::endl;
    std::cin.get();

    // Remove the sample listener when done
    controller.removeListener(listener);

    return 0;
}