DIFFUSION_LOOKUP = {
    'cond': {
        64: {
            'url': 'https://openaipublic.blob.core.windows.net/diffusion/jul-2021/64x64_diffusion.pt',
            "filename": '64x64_diffusion.pt',
            'model_flags': {
                "attention_resolutions": '32,16,8',
                "class_cond": True,
                "diffusion_steps": 1000,
                "dropout": 0.1,
                "image_size": 64,
                "learn_sigma": True,
                "noise_schedule": 'cosine',
                "num_channels": 192,
                "num_head_channels": 64,
                "num_res_blocks": 3,
                "resblock_updown": True,
                "use_new_attention_order": True,
                "use_fp16": True,
                "use_scale_shift_norm": True,
            },
        },
        128: {
            "url": 'https://openaipublic.blob.core.windows.net/diffusion/jul-2021/128x128_diffusion.pt',
            "filename": '128x128_diffusion.pt',
            "model_flags": {
                "attention_resolutions": '32,16,8',
                "class_cond": True,
                "diffusion_steps": 1000,
                "image_size": 128,
                "learn_sigma": True,
                "noise_schedule": 'linear',
                "num_channels": 256,
                "num_heads": 4,
                "num_res_blocks": 2,
                "resblock_updown": True,
                "use_fp16": True,
                "use_scale_shift_norm": True,
            },
        },
        256: {
            "url": "https://openaipublic.blob.core.windows.net/diffusion/jul-2021/256x256_diffusion.pt",
            "filename": '256x256_diffusion.pt',
            "model_flags": {
                "attention_resolutions": "32,16,8",
                "class_cond": True,
                "diffusion_steps": 1000,
                "image_size": 256,
                "learn_sigma": True,
                "noise_schedule": "linear",
                "num_channels": 256,
                "num_head_channels": 64,
                "num_res_blocks": 2,
                "resblock_updown": True,
                "use_fp16": True,
                "use_scale_shift_norm": True
            }
        },
        512: {
            "url": "https://openaipublic.blob.core.windows.net/diffusion/jul-2021/512x512_diffusion.pt",
            "filename": '512x512_diffusion.pt',
            "model_flags": {
                'attention_resolutions': '32, 16, 8',
                'class_cond': True,
                'diffusion_steps': 1000,
                'rescale_timesteps': True,
                'timestep_respacing': '1000',
                'image_size': 512,
                'learn_sigma': True,
                'noise_schedule': 'linear',
                'num_channels': 256,
                'num_head_channels': 64,
                'num_res_blocks': 2,
                'resblock_updown': True,
                'use_fp16': True,
                'use_scale_shift_norm': True,
            },
        },
    },
    'uncond': {
        256: {
            "url": "https://openaipublic.blob.core.windows.net/diffusion/jul-2021/256x256_diffusion_uncond.pt",
            "model_flags": {
                "attention_resolutions": "32,16,8",
                "class_cond": False,
                "diffusion_steps": 1000,
                "image_size": 256,
                "learn_sigma": True,
                "noise_schedule": "linear",
                "num_channels": 256,
                "num_head_channels": 64,
                "num_res_blocks": 2,
                "resblock_updown": True,
                "use_fp16": True,
                "use_scale_shift_norm": True
            },
        },
        512: {
            "url": 'https://the-eye.eu/public/AI/models/512x512_diffusion_unconditional_ImageNet/512x512_diffusion_uncond_finetune_008100.pt',
            "model_flags": {
                'attention_resolutions': '32, 16, 8',
                'class_cond': False,
                'diffusion_steps': 1000,
                'rescale_timesteps': True,
                'timestep_respacing': '1000',
                'image_size': 512,
                'learn_sigma': True,
                'noise_schedule': 'linear',
                'num_channels': 256,
                'num_head_channels': 64,
                'num_res_blocks': 2,
                'resblock_updown': True,
                'use_fp16': True,
                'use_scale_shift_norm': True,
            }
        }
    }
}
