num_steps = 30
style_example = [
            [
                'CompVis/stable-diffusion-v1-4',
                'FateZero/data/teaser_car-turn.mp4',
                'a silver jeep driving down a curvy road in the countryside',
                'watercolor painting of a silver jeep driving down a curvy road in the countryside',
                0.8, 
                0.8,
                "watercolor",
                10,
                num_steps,
                7.5,
                # input video argument
                None, 0, 8, 1, 0,0,0,0
                
            ]
            # [
            #     'CompVis/stable-diffusion-v1-4',
            #     'FateZero/data/style/sunflower.mp4',
            #     'a yellow sunflower',
            #     'van gogh style painting of a yellow sunflower',
            #     0.5,
            #     0.5,
            #     'van gogh',
            #     10,
            #     num_steps,
            #     7.5,
            #     None, 0, 8, 1, 0,0,0,0
            # ],
            # [
            #     'CompVis/stable-diffusion-v1-4',
            #     'FateZero/data/style/surf.mp4',
            #     'a man with round helmet surfing on a white wave in blue ocean with a rope',
            #     'The Ukiyo-e style painting of a man with round helmet surfing on a white wave in blue ocean with a rope',
            #     0.9,
            #     0.9,
            #     'Ukiyo-e',
            #     10,
            #     num_steps,
            #     7.5,
            #     None, 0, 8, 1, 0,0,0,0
            # ],
            # [
            #     'CompVis/stable-diffusion-v1-4',
            #     'FateZero/data/style/train.mp4',
            #     'a train traveling down tracks next to a forest filled with trees and flowers and a man on the side of the track',
            #     'a train traveling down tracks next to a forest filled with trees and flowers and a man on the side of the track Makoto Shinkai style',
            #     0.9,
            #     0.9,
            #     'Makoto Shinkai',
            #     10,
            #     num_steps,
            #     7.5,
            #     None, 0, 8, 28, 0,0,0,0
            # ],

            # [
            #     'CompVis/stable-diffusion-v1-4',
            #     'FateZero/data/attribute/swan_swarov.mp4',
            #     'a black swan with a red beak swimming in a river near a wall and bushes',
            #     'a Swarovski crystal swan with a red beak swimming in a river near a wall and bushes',
            #     0.8,
            #     0.6,
            #     'Swarovski crystal',
            #     10,
            #     num_steps,
            #     7.5,
            #     None, 0, 8, 1, 0,0,0,0
            # ],
            # [
            #     'CompVis/stable-diffusion-v1-4',
            #     'FateZero/data/attribute/squirrel_carrot.mp4',
            #     'A squirrel is eating a carrot',
            #     'A rabbit is eating a eggplant',
            #     0.5,
            #     0.5,
            #     'rabbit eggplant',
            #     10,
            #     num_steps,
            #     7.5,
            #     None, 0, 8, 1, 0,0,0,0
            # ],

]