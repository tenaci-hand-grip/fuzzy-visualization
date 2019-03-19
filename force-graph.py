#!/usr/bin/python3

import matplotlib.pyplot as plt
import json

OUTPUT_DIR = 'output'

with open('membership-functions.json', 'r') as f:
    data = json.load(f)

    ax = plt.subplot(111)

    no_force_x = data['thumbForce']['noForce_x']
    no_force_y = data['thumbForce']['noForce_y']
    ax.plot(no_force_x, no_force_y, label='No Force')

    print("no_force: {}".format(no_force_x))

    light_force_x = data['thumbForce']['lightForce_x']
    light_force_y = data['thumbForce']['lightForce_y']
    ax.plot(light_force_x, light_force_y, label='Light Force')

    print("light_force: {}".format(light_force_x))

    medium_force_x = data['thumbForce']['mediumForce_x']
    medium_force_y = data['thumbForce']['mediumForce_y']
    ax.plot(medium_force_x, medium_force_y, label='Medium Force')

    print("medium_force: {}".format(medium_force_x))

    high_force_x = data['thumbForce']['highForce_x']
    high_force_y = data['thumbForce']['highForce_y']
    ax.plot(high_force_x, high_force_y, label='High Force')

    print("high_force: {}".format(high_force_x))


    # Shrink current axis by 20%
    box = ax.get_position()
    ax.set_position([box.x0, box.y0, box.width * 0.8, box.height])

    ax.set_title('Grip Force Membership Functions')
    ax.set_xlabel("Force (g)")
    ax.set_ylabel("Degree of Membership")
    ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))

    plt.savefig('{}/force-membership.png'.format(OUTPUT_DIR), dpi=300)
    plt.savefig('{}/force-membership.pdf'.format(OUTPUT_DIR))

    plt.show()