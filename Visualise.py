# Visualise.py
# Author: Leo Li

# Python 3
# coding: utf-8
# Python 3.10

# Imports
import sys
import Parser
import Calculator
import Plotter
import os

# Program entry point
if __name__ == '__main__' :
    # Check for arguments error
    if len(sys.argv) < 5:
        print('Usage Error: joint interval dimension filename')
        exit(1)

    # Check file type
    if not sys.argv[4].endswith('.json'):
        print('Usage Error: requires json file')
        exit(1)

    # Check dimensions type
    if not sys.argv[3].lower() == '2d' and not sys.argv[3].lower() == '3d':
        print('Usage Error: dimension must be "2d" or "3d"')
        exit(1)

    # Get variables
    joint = sys.argv[1]
    interval = sys.argv[2]
    dimension = sys.argv[3]
    filename = sys.argv[4]

    # Check argv
    if '-h' in sys.argv:
        print('Help')
        print(' -h  : Print help')
        print(' -i  : Ignore erroneous keypoints')
        print(' -w  : Print warnings')
        print(' -s  : Save parsed json data')
        print(' -S  : Save visualisation graph')

    warnings = False
    if '-w' in sys.argv:
        warnings = True

    # Parse input file
    ignore = False
    if '-i' in sys.argv:
        ignore = True

    # Parse input file into form we need
    # @param joint, filename, shouldIgnore, shouldWarn
    parser = Parser.Parser(joint, filename, ignore, warnings)
    # @return numFrames, leftUpperPoints, leftMiddlePoints, leftLowerPoints, rightUpperPoints, rightMiddlePoints, rightLowerPoints
    numFrames, leftUpperPoints, leftMiddlePoints, leftLowerPoints, rightUpperPoints, rightMiddlePoints, rightLowerPoints = parser.parse()

    # Calculate angles
    # @param numFrames, leftUpperPoints, leftMiddlePoints, leftLowerPoints, rightUpperPoints, rightMiddlePoints, rightLowerPoints
    calculator = Calculator.Calculator(numFrames, leftUpperPoints, leftMiddlePoints, leftLowerPoints, rightUpperPoints, rightMiddlePoints, rightLowerPoints)
    # @return leftJointRoll, leftJointPitch, leftJointYaw, rightJointRoll, rightJointPitch, rightJointYaw, left3d, right3d
    leftJointRoll, leftJointPitch, leftJointYaw, rightJointRoll, rightJointPitch, rightJointYaw, left3d, right3d = calculator.Calculate()

    # Plot
    # @param numFrames, joint, interval ,leftJointRoll, leftJointPitch, leftJointYaw, rightJointRoll, rightJointPitch, rightJointYaw, left3d, right3d
    plotter = Plotter.Plotter(numFrames, joint, interval, leftJointRoll, leftJointPitch, leftJointYaw, rightJointRoll, rightJointPitch, rightJointYaw, left3d, right3d)
    if dimension == '2d':
        plotter.plot2d()
        plotter.markPlots()
    elif dimension == '3d':
        plotter.plot3d()

    if '-S' in sys.argv:
        rawFilename, _ = os.path.splitext(os.path.basename(filename))
        plotter.save(dimension, rawFilename + '_angle_visulisation')
    else:
        plotter.show()

    # Check argv
    if '-s' in sys.argv:
        filenameIndex = sys.argv.index('-s') + 1
        parser.save()

