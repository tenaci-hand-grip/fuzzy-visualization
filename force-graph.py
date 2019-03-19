#!/usr/bin/python3

import matplotlib.pyplot as plt
import json

OUTPUT_DIR = 'output'
digits = ['thumbForce', 'indexForce']

with open('membership-functions.json', 'r') as f:
    data = json.load(f)

    for digit in digits:
        ax = plt.subplot(111)

        no_force_x = data[digit]['noForce_x']
        no_force_y = data[digit]['noForce_y']
        ax.plot(no_force_x, no_force_y, label='No Force')

        print("{} - no_force: {}".format(digit, no_force_x))

        light_force_x = data[digit]['lightForce_x']
        light_force_y = data[digit]['lightForce_y']
        ax.plot(light_force_x, light_force_y, label='Light Force')

        print("{} - light_force: {}".format(digit, light_force_x))

        medium_force_x = data[digit]['mediumForce_x']
        medium_force_y = data[digit]['mediumForce_y']
        ax.plot(medium_force_x, medium_force_y, label='Medium Force')

        print("{} - medium_force: {}".format(digit, medium_force_x))

        high_force_x = data[digit]['highForce_x']
        high_force_y = data[digit]['highForce_y']
        ax.plot(high_force_x, high_force_y, label='High Force')

        print("{} - high_force: {}".format(digit, high_force_x))


        # Shrink current axis by 20%
        box = ax.get_position()
        ax.set_position([box.x0, box.y0, box.width * 0.8, box.height])

        ax.set_title('Grip Force Membership Functions - {}'.format(digit))
        ax.set_xlabel("Force (g)")
        ax.set_ylabel("Degree of Membership")
        ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))

        plt.savefig('{}/force-membership-{}.png'.format(OUTPUT_DIR, digit), dpi=300)
        plt.savefig('{}/force-membership-{}.pdf'.format(OUTPUT_DIR, digit))

        plt.show()