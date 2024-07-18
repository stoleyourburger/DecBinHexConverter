from flask import Flask
from markupsafe import escape


app = Flask(__name__)


# Health check
@app.route("/health")
def health_check():
    return "OK"


@app.route("/convert/<value>/<input_format>/<output_format>")
def convert(value, input_format, output_format):

    if input_format == output_format:
        return escape(value)

    try:
        match (escape(input_format), escape(output_format)):
            case ("bin", "dec"):
                return str(int(value, 2))
            case ("bin", "hex"):
                return hex((int(value, 2))).replace("0x", "").upper()
            case ("dec", "bin"):
                return bin(int(value)).replace("0b", "")
            case ("dec", "hex"):
                return hex((int(value, 10))).replace("0x", "").upper()
            case ("hex", "bin"):
                return bin(int(value, 16)).replace("0b", "")
            case ("hex", "dec"):
                return str(int(value, 16))
            case _:
                return wrong_endpoint()

    except ValueError:
        return f"Value '{value}' can't be converted from {input_format} to {output_format}."


# Wrong endpoint handler (Usage guide)
@app.errorhandler(404)
def wrong_endpoint():
    return """
        Binary <=> Decimal <=> Hexadecimal Converter  <br>
<br>
This tool allows you to convert values between binary, decimal and hexadecimal formats. <br> 
To use the converter, you need to specify the initial value, input format, and output format in the following path structure: <br>
<br>
/convert/value/input_format/output_format <br>
<br>
-------- Usage Guide --------<br>
<br>
Arguments to use: <br>
<br>
value: The alphanumeric value to be converted. This must be in the format specified by input_format. <br>
<br>
input_format: The format of the input value. Possible values: <br>
        bin: Binary (base-2) <br>
        dec: Decimal (base-10) <br>
        hex: Hexadecimal (base-16) <br>
<br>
output_format: The desired format for the output value. Possible values: <br>
        bin: Binary (base-2) <br>
        dec: Decimal (base-10) <br>
        hex: Hexadecimal (base-16) <br>
<br>
Ensure that the value matches the specified input_format. For example, if input_format is bin, the value should be a binary number. <br>
<br>
-------- Example 1 -------- <br>
<br>
/convert/10111010/bin/dec <br>
This will convert the binary value 10111010 to its decimal equivalent. <br>
<br>
-------- Example 2 -------- <br>
<br>
/convert/255/dec/hex <br>
This will convert the decimal value 255 to its hexadecimal equivalent. <br>
<br>
-------- Example 3 -------- <br>
<br>
/convert/A1FF/hex/bin <br>
This will convert the hexadecimal value A1FF to its binary equivalent. <br>
"""


if __name__ == "__main__":
    app.run(debug=True, port=8080)
