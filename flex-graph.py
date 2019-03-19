#!/usr/bin/python3

import matplotlib.pyplot as plt
import json

OUTPUT_DIR = 'output'

with open('membership-functions.json', 'r') as f:
    data = json.load(f)

    ax = plt.subplot(111)

    not_flexed_x = data['thumbFlex']['notFlexed_x']
    not_flexed_y = data['thumbFlex']['notFlexed_y']
    ax.plot(not_flexed_x, not_flexed_y, label='Not Flexed')

    # print("not_flexed: {}, {}, {}, {}".format(0, 0, not_flexed_center+offset, 25-offset2))
    print("not_flexed: {}".format(not_flexed_x))

    partially_flexed_x = data['thumbFlex']['partiallyFlexed_x']
    partially_flexed_y = data['thumbFlex']['partiallyFlexed_y']
    ax.plot(partially_flexed_x, partially_flexed_y, label='Partially Flexed')

    # print("partially_flexed: {}, {}, {}, {}".format(0+offset2, partially_flexed_center-offset, partially_flexed_center+offset, 50-offset2))
    print("partially_flexed: {}".format(partially_flexed_x))

    half_flexed_x = data['thumbFlex']['halfFlexed_x']
    half_flexed_y = data['thumbFlex']['halfFlexed_y']
    ax.plot(half_flexed_x, half_flexed_y, label='Half Flexed')

    # print("half_flexed: {}, {}, {}, {}".format(25+offset2, half_flexed_center-offset, half_flexed_center+offset, 75-offset2))
    print("half_flexed: {}".format(half_flexed_x))

    mostly_flexed_x = data['thumbFlex']['mostlyFlexed_x']
    mostly_flexed_y = data['thumbFlex']['mostlyFlexed_y']
    ax.plot(mostly_flexed_x, mostly_flexed_y, label='Mostly Flexed')

    # print("mostly_flexed: {}, {}, {}, {}".format(50+offset2, mostly_flexed_center-offset, mostly_flexed_center+offset, 100-offset2))
    print("mostly_flexed: {}".format(mostly_flexed_x))

    fully_flexed_x = data['thumbFlex']['fullyFlexed_x']
    fully_flexed_y = data['thumbFlex']['fullyFlexed_y']
    ax.plot(fully_flexed_x, fully_flexed_y, label='Fully Flexed')

    # print("fully_flexed: {}, {}, {}, {}".format(75+offset2, fully_flexed_center-offset, 100, 100))
    print("fully_flexed: {}".format(fully_flexed_x))

    # Shrink current axis by 20%
    box = ax.get_position()
    ax.set_position([box.x0, box.y0, box.width * 0.8, box.height])

    ax.set_title('Flex Membership Functions')
    ax.set_xlabel("Flex (degrees)")
    ax.set_ylabel("Degree of Membership")
    ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))

    plt.savefig('{}/flex-membership.png'.format(OUTPUT_DIR), dpi=300)
    plt.savefig('{}/flex-membership.pdf'.format(OUTPUT_DIR))

    plt.show()