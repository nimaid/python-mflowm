import sys

import cv2
import argparse

import mflowm
from mflowm.helpers import file_path
from mflowm import MotionFlowMulti, CompositeMode, VideoReader


def convert_video(
        filename,
        mode: CompositeMode,
        trails: bool = False,
        fade_speed: float | None = 2,
        windows_balance: bool = False,
        pre_scale: float = 1,
        display_scale: float = 1,
        scale_method=cv2.INTER_NEAREST
):
    # Create the VideoReader
    video_reader = VideoReader(filename, scale=pre_scale)

    # Create the MotionFlowMulti object
    mfm = MotionFlowMulti(
        video_reader,
        mode=mode,
        trails=trails,
        fade_speed=fade_speed,
        windows_balance=windows_balance,
    )

    mfm.convert_to_file(
        output_scale=(1 / pre_scale),
        display_scale=(1 / pre_scale) * display_scale,
        output_scale_method=scale_method,
        display_scale_method=scale_method
    )


# Parse arguments
def parse_args(args):
    parser = argparse.ArgumentParser(
        description=f"{mflowm.__doc__}\n\n"
                    f"Valid parameters are shown in {{braces}}\n"
                    f"Default parameters are shown in [brackets].",
        formatter_class=argparse.RawDescriptionHelpFormatter
    )

    parser.add_argument(
        "-i", "--input", dest="video_file",
        type=file_path, required=True,
        help="the video file to process"
    )

    parser.add_argument(
        "-m", "--mode", dest="mode",
        type=str, required=True,
        help="the composite mode to use {{{values}}}".format(
            values=", ".join([x.name for x in CompositeMode])
        )
    )

    parser.add_argument(
        "-t", "--trails", dest="deaw_trails",
        type=bool, required=False, default=False,
        help=f"if we should draw trails or not [{False}]"
    )





    parser.add_argument("-1", "--first", dest="first_arg", type=float, required=True,
                        help="the first argument"
                        )

    parser.add_argument("-2", "--second", dest="second_arg", type=float, required=False, default=1.0,
                        help="the second argument [{default}]".format(
                            default=DEFAULTS["second"])
                        )

    parser.add_argument("-o", "--operation", dest="opcode", type=str, required=False, default="+",
                        help="the operation to perform on the arguments, either {{{values}}} [{default}]".format(
                            values=", ".join([x.value for x in OpCode]),
                        default=DEFAULTS["opcode"].value)
                        )

    parsed_args = parser.parse_args(args)

    # Interpret string arguments
    if parsed_args.opcode is not None:
        if parsed_args.opcode in [x.value for x in OpCode]:
            parsed_args.opcode = OpCode(parsed_args.opcode)
        else:
            parser.error(f"\"{parsed_args.opcode}\" is not a valid opcode")

    return parsed_args


def main(args):
    parsed_args = parse_args(args)




def run():
    main(sys.argv[1:])
