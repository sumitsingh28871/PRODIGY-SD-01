# Temperature Converter Program

Welcome to the Temperature Converter Program. This simple utility converts temperatures between Celsius, Fahrenheit, and Kelvin.

## Description

This program prompts the user to enter a temperature value and its unit (Celsius, Fahrenheit, or Kelvin) and then converts it to the other two units. The program handles the following conversions:

- Celsius to Fahrenheit
- Celsius to Kelvin
- Fahrenheit to Celsius
- Fahrenheit to Kelvin
- Kelvin to Celsius
- Kelvin to Fahrenheit

## Usage

### Prerequisites

- Python 3.x

### Running the Program

1. **Clone the repository or copy the script to your local machine.**

2. **Open a terminal or command prompt.**

3. **Navigate to the directory containing the script.**

4. **Run the script using Python:**

    ```sh
    python temperature_converter.py
    ```

5. **Follow the on-screen instructions:**

    - Enter the temperature value.
    - Specify the unit of the temperature (C for Celsius, F for Fahrenheit, K for Kelvin).

6. **View the converted temperature values in the other units.**

## Code Overview

The program defines several functions to perform temperature conversions:

- `celsius_to_fahrenheit(celsius)`: Converts Celsius to Fahrenheit.
- `celsius_to_kelvin(celsius)`: Converts Celsius to Kelvin.
- `fahrenheit_to_celsius(fahrenheit)`: Converts Fahrenheit to Celsius.
- `fahrenheit_to_kelvin(fahrenheit)`: Converts Fahrenheit to Kelvin.
- `kelvin_to_celsius(kelvin)`: Converts Kelvin to Celsius.
- `kelvin_to_fahrenheit(kelvin)`: Converts Kelvin to Fahrenheit.

The main function, `temp_converter()`, handles user input and calls the appropriate conversion functions based on the user's input.


