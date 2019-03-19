#!/usr/bin/python3

import matplotlib.pyplot as plt
import json

OUTPUT_DIR = 'output'
digits = ['thumbFlex', 'indexFlex', 'pinkyFlex']

with open('membership-functions.json', 'r') as f:
    data = json.load(f)

    for digit in digits:
        ax = plt.subplot(111)

        not_flexed_x = data[digit]['notFlexed_x']
        not_flexed_y = data[digit]['notFlexed_y']
        ax.plot(not_flexed_x, not_flexed_y, label='Not Flexed')

        print("{} - not_flexed: {}".format(digit, not_flexed_x))

        partially_flexed_x = data[digit]['partiallyFlexed_x']
        partially_flexed_y = data[digit]['partiallyFlexed_y']
        ax.plot(partially_flexed_x, partially_flexed_y, label='Partially Flexed')

        print("{} - partially_flexed: {}".format(digit, partially_flexed_x))

        half_flexed_x = data[digit]['halfFlexed_x']
        half_flexed_y = data[digit]['halfFlexed_y']
        ax.plot(half_flexed_x, half_flexed_y, label='Half Flexed')

        print("{} - half_flexed: {}".format(digit, half_flexed_x))

        mostly_flexed_x = data[digit]['mostlyFlexed_x']
        mostly_flexed_y = data[digit]['mostlyFlexed_y']
        ax.plot(mostly_flexed_x, mostly_flexed_y, label='Mostly Flexed')

        print("{} - mostly_flexed: {}".format(digit, mostly_flexed_x))

        fully_flexed_x = data[digit]['fullyFlexed_x']
        fully_flexed_y = data[digit]['fullyFlexed_y']
        ax.plot(fully_flexed_x, fully_flexed_y, label='Fully Flexed')

        print("{} - fully_flexed: {}".format(digit, fully_flexed_x))

        # Shrink current axis by 20%
        box = ax.get_position()
        ax.set_position([box.x0, box.y0, box.width * 0.8, box.height])

        ax.set_title('Flex Membership Functions - {}'.format(digit))
        ax.set_xlabel("Flex (degrees)")
        ax.set_ylabel("Degree of Membership")
        ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))

        plt.savefig('{}/flex-membership-{}.png'.format(OUTPUT_DIR, digit), dpi=300)
        plt.savefig('{}/flex-membership-{}.pdf'.format(OUTPUT_DIR, digit))

        plt.show()