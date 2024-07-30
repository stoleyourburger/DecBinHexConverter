from flask import Flask, abort
from markupsafe import escape
import enum


app = Flask(__name__)


# Health check
@app.route("/health")
def health_check():
    return "OK."


class Bases(enum.IntEnum):
    bin = 2
    dec = 10
    hex = 16


@app.route("/convert/<value>/<input_format>/<output_format>")
def from_dec(value, input_format, output_format):

    try:
        decimal_value = int(value, Bases[escape(input_format)])
        match escape(output_format):
            case "bin":
                return f"{decimal_value:b}"
            case "hex":
                return f"{decimal_value:x}".upper()
            case "dec":
                return f"{decimal_value}"
            case _:
                abort(400, description=f"Unknown output format: {output_format}")

    except KeyError:
        abort(400, description=f"Unknown input format: {input_format}")

    except ValueError:
        abort(
            400,
            description=f"Value '{value}' can't be converted from {input_format} to {output_format}.",
        )


@app.errorhandler(404)
def wrong_endpoint(e):
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
    app.run(host="0.0.0.0", port=8080, debug=True)
