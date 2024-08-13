from source.mission.template.mission_just_collect import MissionJustCollect

tlp2m_default_value = {'start_position': [-4274.432, -952.32], 'end_position': [-4110.848, -664.32], 'position_list': [{'id': 1, 'motion': 'WALKING', 'position': [-4274.432, -952.32]}, {'id': 2, 'motion': 'WALKING', 'position': [-4276.224, -951.808]}, {'id': 3, 'motion': 'WALKING', 'position': [-4280.064, -950.272]}, {'id': 4, 'motion': 'WALKING', 'position': [-4285.44, -945.664]}, {'id': 5, 'motion': 'WALKING', 'position': [-4290.56, -941.568]}, {'id': 6, 'motion': 'WALKING', 'position': [-4294.144, -940.032]}, {'id': 7, 'motion': 'WALKING', 'position': [-4297.216, -937.728]}, {'id': 8, 'motion': 'FLYING', 'position': [-4300.8, -935.936]}, {'id': 9, 'motion': 'FLYING', 'position': [-4304.128, -934.4]}, {'id': 10, 'motion': 'FLYING', 'position': [-4307.968, -932.864]}, {'id': 11, 'motion': 'FLYING', 'position': [-4310.272, -932.608]}, {'id': 12, 'motion': 'FLYING', 'position': [-4314.112, -931.584]}, {'id': 13, 'motion': 'FLYING', 'position': [-4317.952, -931.072]}, {'id': 14, 'motion': 'FLYING', 'position': [-4322.048, -930.816]}, {'id': 15, 'motion': 'FLYING', 'position': [-4324.096, -930.816]}, {'id': 16, 'motion': 'FLYING', 'position': [-4327.936, -931.328]}, {'id': 17, 'motion': 'FLYING', 'position': [-4332.032, -932.096]}, {'id': 18, 'motion': 'FLYING', 'position': [-4336.128, -932.864]}, {'id': 19, 'motion': 'FLYING', 'position': [-4337.92, -933.12]}, {'id': 20, 'motion': 'FLYING', 'position': [-4341.76, -934.144]}, {'id': 21, 'motion': 'FLYING', 'position': [-4345.856, -934.656]}, {'id': 22, 'motion': 'FLYING', 'position': [-4347.648, -934.912]}, {'id': 23, 'motion': 'FLYING', 'position': [-4351.744, -935.68]}, {'id': 24, 'motion': 'FLYING', 'position': [-4356.096, -936.192]}, {'id': 25, 'motion': 'FLYING', 'position': [-4359.68, -936.704]}, {'id': 26, 'motion': 'FLYING', 'position': [-4363.52, -937.216]}, {'id': 27, 'motion': 'FLYING', 'position': [-4365.824, -937.472]}, {'id': 28, 'motion': 'FLYING', 'position': [-4369.408, -938.496]}, {'id': 29, 'motion': 'FLYING', 'position': [-4373.248, -939.264]}, {'id': 30, 'motion': 'FLYING', 'position': [-4377.344, -940.032]}, {'id': 31, 'motion': 'FLYING', 'position': [-4378.88, -940.288]}, {'id': 32, 'motion': 'FLYING', 'position': [-4382.976, -941.568]}, {'id': 33, 'motion': 'FLYING', 'position': [-4384.512, -942.336]}, {'id': 34, 'motion': 'FLYING', 'position': [-4388.096, -944.384]}, {'id': 35, 'motion': 'FLYING', 'position': [-4391.936, -945.92]}, {'id': 36, 'motion': 'FLYING', 'position': [-4395.776, -946.944]}, {'id': 37, 'motion': 'FLYING', 'position': [-4399.36, -948.224]}, {'id': 38, 'motion': 'FLYING', 'position': [-4403.2, -949.504]}, {'id': 39, 'motion': 'FLYING', 'position': [-4405.248, -950.016]}, {'id': 40, 'motion': 'FLYING', 'position': [-4408.832, -950.784]}, {'id': 41, 'motion': 'FLYING', 'position': [-4411.136, -951.296]}, {'id': 42, 'motion': 'FLYING', 'position': [-4411.136, -951.296]}, {'id': 43, 'motion': 'WALKING', 'position': [-4411.648, -950.016]}, {'id': 44, 'motion': 'WALKING', 'position': [-4414.208, -946.944]}, {'id': 45, 'motion': 'WALKING', 'position': [-4416.0, -945.92]}, {'id': 46, 'motion': 'WALKING', 'position': [-4417.792, -944.384]}, {'id': 47, 'motion': 'WALKING', 'position': [-4419.072, -942.592]}, {'id': 48, 'motion': 'WALKING', 'position': [-4422.4, -940.544]}, {'id': 49, 'motion': 'WALKING', 'position': [-4423.68, -939.008]}, {'id': 50, 'motion': 'WALKING', 'position': [-4427.008, -936.192]}, {'id': 51, 'motion': 'WALKING', 'position': [-4428.032, -934.912]}, {'id': 52, 'motion': 'WALKING', 'position': [-4430.336, -931.328]}, {'id': 53, 'motion': 'WALKING', 'position': [-4432.128, -930.048]}, {'id': 54, 'motion': 'WALKING', 'position': [-4434.432, -926.464]}, {'id': 55, 'motion': 'WALKING', 'position': [-4435.712, -925.184]}, {'id': 56, 'motion': 'WALKING', 'position': [-4438.528, -921.856]}, {'id': 57, 'motion': 'WALKING', 'position': [-4440.576, -919.296]}, {'id': 58, 'motion': 'WALKING', 'position': [-4442.112, -917.248]}, {'id': 59, 'motion': 'WALKING', 'position': [-4443.392, -915.712]}, {'id': 60, 'motion': 'WALKING', 'position': [-4445.696, -912.384]}, {'id': 61, 'motion': 'WALKING', 'position': [-4447.232, -910.848]}, {'id': 62, 'motion': 'WALKING', 'position': [-4448.512, -909.568]}, {'id': 63, 'motion': 'WALKING', 'position': [-4449.536, -907.52]}, {'id': 64, 'motion': 'WALKING', 'position': [-4452.608, -904.704]}, {'id': 65, 'motion': 'WALKING', 'position': [-4453.888, -902.912]}, {'id': 66, 'motion': 'WALKING', 'position': [-4456.192, -899.84]}, {'id': 67, 'motion': 'WALKING', 'position': [-4457.728, -898.048]}, {'id': 68, 'motion': 'WALKING', 'position': [-4457.984, -898.048]}, {'id': 69, 'motion': 'WALKING', 'position': [-4459.008, -896.256]}, {'id': 70, 'motion': 'WALKING', 'position': [-4460.544, -896.512]}, {'id': 71, 'motion': 'WALKING', 'position': [-4464.896, -897.536]}, {'id': 72, 'motion': 'WALKING', 'position': [-4466.944, -898.048]}, {'id': 73, 'motion': 'WALKING', 'position': [-4470.784, -899.072]}, {'id': 74, 'motion': 'WALKING', 'position': [-4473.344, -899.328]}, {'id': 75, 'motion': 'WALKING', 'position': [-4475.136, -899.84]}, {'id': 76, 'motion': 'WALKING', 'position': [-4479.488, -900.096]}, {'id': 77, 'motion': 'SWIMMING', 'position': [-4481.536, -900.352]}, {'id': 78, 'motion': 'WALKING', 'position': [-4483.84, -900.864]}, {'id': 79, 'motion': 'SWIMMING', 'position': [-4487.424, -901.376]}, {'id': 80, 'motion': 'SWIMMING', 'position': [-4487.424, -901.376]}, {'id': 81, 'motion': 'SWIMMING', 'position': [-4489.472, -901.888]}, {'id': 82, 'motion': 'SWIMMING', 'position': [-4489.472, -901.888]}, {'id': 83, 'motion': 'SWIMMING', 'position': [-4491.008, -902.4]}, {'id': 84, 'motion': 'SWIMMING', 'position': [-4491.264, -902.4]}, {'id': 85, 'motion': 'SWIMMING', 'position': [-4493.312, -902.656]}, {'id': 86, 'motion': 'SWIMMING', 'position': [-4493.312, -902.656]}, {'id': 87, 'motion': 'SWIMMING', 'position': [-4495.104, -902.912]}, {'id': 88, 'motion': 'SWIMMING', 'position': [-4495.104, -902.912]}, {'id': 89, 'motion': 'SWIMMING', 'position': [-4496.896, -903.168]}, {'id': 90, 'motion': 'SWIMMING', 'position': [-4499.2, -903.68]}, {'id': 91, 'motion': 'SWIMMING', 'position': [-4500.736, -903.936]}, {'id': 92, 'motion': 'SWIMMING', 'position': [-4505.088, -904.448]}, {'id': 93, 'motion': 'SWIMMING', 'position': [-4505.088, -904.448]}, {'id': 94, 'motion': 'SWIMMING', 'position': [-4509.44, -904.704]}, {'id': 95, 'motion': 'SWIMMING', 'position': [-4510.976, -904.96]}, {'id': 96, 'motion': 'SWIMMING', 'position': [-4513.536, -905.216]}, {'id': 97, 'motion': 'SWIMMING', 'position': [-4515.584, -905.216]}, {'id': 98, 'motion': 'SWIMMING', 'position': [-4517.632, -905.472]}, {'id': 99, 'motion': 'SWIMMING', 'position': [-4520.192, -905.728]}, {'id': 100, 'motion': 'SWIMMING', 'position': [-4521.728, -905.728]}, {'id': 101, 'motion': 'SWIMMING', 'position': [-4524.288, -905.984]}, {'id': 102, 'motion': 'SWIMMING', 'position': [-4526.08, -906.24]}, {'id': 103, 'motion': 'SWIMMING', 'position': [-4528.128, -906.496]}, {'id': 104, 'motion': 'SWIMMING', 'position': [-4530.432, -906.752]}, {'id': 105, 'motion': 'SWIMMING', 'position': [-4532.224, -907.264]}, {'id': 106, 'motion': 'SWIMMING', 'position': [-4534.528, -907.52]}, {'id': 107, 'motion': 'SWIMMING', 'position': [-4536.576, -907.776]}, {'id': 108, 'motion': 'SWIMMING', 'position': [-4538.624, -908.288]}, {'id': 109, 'motion': 'SWIMMING', 'position': [-4540.928, -908.8]}, {'id': 110, 'motion': 'SWIMMING', 'position': [-4542.464, -909.056]}, {'id': 111, 'motion': 'SWIMMING', 'position': [-4545.024, -909.312]}, {'id': 112, 'motion': 'SWIMMING', 'position': [-4546.816, -909.568]}, {'id': 113, 'motion': 'SWIMMING', 'position': [-4548.864, -909.824]}, {'id': 114, 'motion': 'SWIMMING', 'position': [-4551.168, -910.08]}, {'id': 115, 'motion': 'SWIMMING', 'position': [-4552.96, -910.08]}, {'id': 116, 'motion': 'WALKING', 'position': [-4555.52, -910.336]}, {'id': 117, 'motion': 'WALKING', 'position': [-4557.312, -910.592]}, {'id': 118, 'motion': 'WALKING', 'position': [-4561.408, -910.848]}, {'id': 119, 'motion': 'WALKING', 'position': [-4567.04, -911.616]}, {'id': 120, 'motion': 'WALKING', 'position': [-4567.04, -911.616]}, {'id': 121, 'motion': 'WALKING', 'position': [-4569.088, -908.288]}, {'id': 122, 'motion': 'WALKING', 'position': [-4571.136, -904.192]}, {'id': 123, 'motion': 'WALKING', 'position': [-4572.672, -899.84]}, {'id': 124, 'motion': 'WALKING', 'position': [-4574.208, -895.488]}, {'id': 125, 'motion': 'WALKING', 'position': [-4576.256, -891.904]}, {'id': 126, 'motion': 'WALKING', 'position': [-4577.024, -889.856]}, {'id': 127, 'motion': 'WALKING', 'position': [-4577.536, -888.32]}, {'id': 128, 'motion': 'WALKING', 'position': [-4577.536, -888.32]}, {'id': 129, 'motion': 'WALKING', 'position': [-4580.096, -884.736]}, {'id': 130, 'motion': 'WALKING', 'position': [-4585.216, -880.128]}, {'id': 131, 'motion': 'WALKING', 'position': [-4590.08, -875.776]}, {'id': 132, 'motion': 'WALKING', 'position': [-4593.152, -873.472]}, {'id': 133, 'motion': 'WALKING', 'position': [-4596.736, -869.888]}, {'id': 134, 'motion': 'WALKING', 'position': [-4599.552, -867.584]}, {'id': 135, 'motion': 'WALKING', 'position': [-4603.136, -864.256]}, {'id': 136, 'motion': 'WALKING', 'position': [-4604.672, -862.976]}, {'id': 137, 'motion': 'WALKING', 'position': [-4608.0, -859.904]}, {'id': 138, 'motion': 'WALKING', 'position': [-4611.84, -857.856]}, {'id': 139, 'motion': 'WALKING', 'position': [-4613.376, -856.32]}, {'id': 140, 'motion': 'WALKING', 'position': [-4617.216, -853.504]}, {'id': 141, 'motion': 'WALKING', 'position': [-4620.288, -850.432]}, {'id': 142, 'motion': 'WALKING', 'position': [-4623.616, -848.128]}, {'id': 143, 'motion': 'WALKING', 'position': [-4626.432, -845.568]}, {'id': 144, 'motion': 'WALKING', 'position': [-4629.76, -843.008]}, {'id': 145, 'motion': 'WALKING', 'position': [-4631.552, -841.728]}, {'id': 146, 'motion': 'WALKING', 'position': [-4636.16, -837.888]}, {'id': 147, 'motion': 'WALKING', 'position': [-4637.696, -836.608]}, {'id': 148, 'motion': 'WALKING', 'position': [-4641.024, -833.792]}, {'id': 149, 'motion': 'WALKING', 'position': [-4644.608, -831.232]}, {'id': 150, 'motion': 'WALKING', 'position': [-4648.448, -828.416]}, {'id': 151, 'motion': 'WALKING', 'position': [-4649.728, -827.648]}, {'id': 152, 'motion': 'WALKING', 'position': [-4649.728, -827.648]}, {'id': 153, 'motion': 'WALKING', 'position': [-4651.264, -826.112]}, {'id': 154, 'motion': 'WALKING', 'position': [-4651.264, -826.112]}, {'id': 155, 'motion': 'WALKING', 'position': [-4653.824, -826.368]}, {'id': 156, 'motion': 'WALKING', 'position': [-4659.968, -826.624]}, {'id': 157, 'motion': 'WALKING', 'position': [-4666.624, -826.624]}, {'id': 158, 'motion': 'WALKING', 'position': [-4670.72, -826.624]}, {'id': 159, 'motion': 'WALKING', 'position': [-4675.072, -826.88]}, {'id': 160, 'motion': 'WALKING', 'position': [-4679.68, -826.88]}, {'id': 161, 'motion': 'WALKING', 'position': [-4684.288, -826.88]}, {'id': 162, 'motion': 'WALKING', 'position': [-4688.384, -827.136]}, {'id': 163, 'motion': 'WALKING', 'position': [-4692.48, -827.136]}, {'id': 164, 'motion': 'WALKING', 'position': [-4694.784, -827.136]}, {'id': 165, 'motion': 'WALKING', 'position': [-4699.392, -827.136]}, {'id': 166, 'motion': 'WALKING', 'position': [-4704.0, -827.136]}, {'id': 167, 'motion': 'WALKING', 'position': [-4708.096, -826.88]}, {'id': 168, 'motion': 'WALKING', 'position': [-4712.448, -826.624]}, {'id': 169, 'motion': 'WALKING', 'position': [-4716.544, -826.368]}, {'id': 170, 'motion': 'WALKING', 'position': [-4720.896, -825.856]}, {'id': 171, 'motion': 'WALKING', 'position': [-4722.688, -825.6]}, {'id': 172, 'motion': 'WALKING', 'position': [-4727.04, -825.088]}, {'id': 173, 'motion': 'WALKING', 'position': [-4731.648, -824.832]}, {'id': 174, 'motion': 'WALKING', 'position': [-4736.256, -824.32]}, {'id': 175, 'motion': 'WALKING', 'position': [-4740.352, -823.808]}, {'id': 176, 'motion': 'WALKING', 'position': [-4744.448, -823.552]}, {'id': 177, 'motion': 'WALKING', 'position': [-4748.8, -823.296]}, {'id': 178, 'motion': 'WALKING', 'position': [-4751.36, -823.04]}, {'id': 179, 'motion': 'WALKING', 'position': [-4755.712, -822.784]}, {'id': 180, 'motion': 'WALKING', 'position': [-4759.808, -822.528]}, {'id': 181, 'motion': 'WALKING', 'position': [-4759.808, -822.528]}, {'id': 182, 'motion': 'WALKING', 'position': [-4761.856, -822.272]}, {'id': 183, 'motion': 'WALKING', 'position': [-4766.464, -817.92]}, {'id': 184, 'motion': 'WALKING', 'position': [-4769.28, -814.592]}, {'id': 185, 'motion': 'WALKING', 'position': [-4772.608, -812.288]}, {'id': 186, 'motion': 'WALKING', 'position': [-4775.936, -808.704]}, {'id': 187, 'motion': 'WALKING', 'position': [-4777.472, -807.68]}, {'id': 188, 'motion': 'WALKING', 'position': [-4780.8, -804.096]}, {'id': 189, 'motion': 'WALKING', 'position': [-4783.616, -801.792]}, {'id': 190, 'motion': 'WALKING', 'position': [-4786.688, -798.464]}, {'id': 191, 'motion': 'WALKING', 'position': [-4788.224, -797.44]}, {'id': 192, 'motion': 'WALKING', 'position': [-4789.76, -795.904]}, {'id': 193, 'motion': 'WALKING', 'position': [-4792.576, -792.832]}, {'id': 194, 'motion': 'WALKING', 'position': [-4794.112, -791.552]}, {'id': 195, 'motion': 'WALKING', 'position': [-4795.904, -789.76]}, {'id': 196, 'motion': 'WALKING', 'position': [-4797.184, -788.224]}, {'id': 197, 'motion': 'WALKING', 'position': [-4797.184, -788.224]}, {'id': 198, 'motion': 'WALKING', 'position': [-4798.72, -787.2]}, {'id': 199, 'motion': 'WALKING', 'position': [-4798.72, -787.2]}, {'id': 200, 'motion': 'WALKING', 'position': [-4793.088, -784.128]}, {'id': 201, 'motion': 'WALKING', 'position': [-4787.2, -781.824]}, {'id': 202, 'motion': 'WALKING', 'position': [-4783.36, -780.288]}, {'id': 203, 'motion': 'WALKING', 'position': [-4779.008, -778.496]}, {'id': 204, 'motion': 'WALKING', 'position': [-4775.424, -777.216]}, {'id': 205, 'motion': 'WALKING', 'position': [-4771.328, -775.936]}, {'id': 206, 'motion': 'WALKING', 'position': [-4769.28, -774.912]}, {'id': 207, 'motion': 'WALKING', 'position': [-4767.232, -773.888]}, {'id': 208, 'motion': 'WALKING', 'position': [-4763.136, -772.352]}, {'id': 209, 'motion': 'WALKING', 'position': [-4761.344, -771.84]}, {'id': 210, 'motion': 'WALKING', 'position': [-4753.152, -768.256]}, {'id': 211, 'motion': 'WALKING', 'position': [-4749.312, -766.976]}, {'id': 212, 'motion': 'WALKING', 'position': [-4743.168, -764.672]}, {'id': 213, 'motion': 'WALKING', 'position': [-4741.376, -763.648]}, {'id': 214, 'motion': 'WALKING', 'position': [-4741.376, -763.648]}, {'id': 215, 'motion': 'WALKING', 'position': [-4739.584, -762.88]}, {'id': 216, 'motion': 'WALKING', 'position': [-4737.28, -762.624]}, {'id': 217, 'motion': 'WALKING', 'position': [-4730.88, -763.904]}, {'id': 218, 'motion': 'WALKING', 'position': [-4724.992, -765.44]}, {'id': 219, 'motion': 'WALKING', 'position': [-4720.64, -766.208]}, {'id': 220, 'motion': 'WALKING', 'position': [-4716.032, -766.72]}, {'id': 221, 'motion': 'WALKING', 'position': [-4711.936, -767.232]}, {'id': 222, 'motion': 'WALKING', 'position': [-4707.328, -768.0]}, {'id': 223, 'motion': 'WALKING', 'position': [-4702.976, -768.768]}, {'id': 224, 'motion': 'WALKING', 'position': [-4699.136, -769.792]}, {'id': 225, 'motion': 'WALKING', 'position': [-4694.784, -770.56]}, {'id': 226, 'motion': 'WALKING', 'position': [-4689.92, -771.328]}, {'id': 227, 'motion': 'WALKING', 'position': [-4687.872, -771.84]}, {'id': 228, 'motion': 'WALKING', 'position': [-4683.52, -772.352]}, {'id': 229, 'motion': 'WALKING', 'position': [-4679.168, -772.864]}, {'id': 230, 'motion': 'WALKING', 'position': [-4674.816, -773.632]}, {'id': 231, 'motion': 'WALKING', 'position': [-4674.816, -773.632]}, {'id': 232, 'motion': 'WALKING', 'position': [-4673.28, -774.144]}, {'id': 233, 'motion': 'WALKING', 'position': [-4673.28, -774.144]}, {'id': 234, 'motion': 'WALKING', 'position': [-4668.672, -772.608]}, {'id': 235, 'motion': 'WALKING', 'position': [-4662.784, -770.048]}, {'id': 236, 'motion': 'WALKING', 'position': [-4658.944, -768.0]}, {'id': 237, 'motion': 'WALKING', 'position': [-4654.848, -766.208]}, {'id': 238, 'motion': 'WALKING', 'position': [-4651.008, -763.904]}, {'id': 239, 'motion': 'WALKING', 'position': [-4651.008, -763.904]}, {'id': 240, 'motion': 'WALKING', 'position': [-4647.424, -761.6]}, {'id': 241, 'motion': 'WALKING', 'position': [-4644.096, -759.296]}, {'id': 242, 'motion': 'WALKING', 'position': [-4642.048, -758.016]}, {'id': 243, 'motion': 'WALKING', 'position': [-4642.048, -758.016]}, {'id': 244, 'motion': 'WALKING', 'position': [-4640.256, -756.992]}, {'id': 245, 'motion': 'WALKING', 'position': [-4638.976, -756.224]}, {'id': 246, 'motion': 'WALKING', 'position': [-4637.696, -755.456]}, {'id': 247, 'motion': 'WALKING', 'position': [-4635.648, -753.92]}, {'id': 248, 'motion': 'WALKING', 'position': [-4634.112, -752.384]}, {'id': 249, 'motion': 'WALKING', 'position': [-4630.784, -750.592]}, {'id': 250, 'motion': 'WALKING', 'position': [-4628.992, -749.312]}, {'id': 251, 'motion': 'WALKING', 'position': [-4627.712, -748.032]}, {'id': 252, 'motion': 'SWIMMING', 'position': [-4625.664, -747.008]}, {'id': 253, 'motion': 'SWIMMING', 'position': [-4622.592, -745.216]}, {'id': 254, 'motion': 'SWIMMING', 'position': [-4622.592, -745.216]}, {'id': 255, 'motion': 'SWIMMING', 'position': [-4620.544, -743.68]}, {'id': 256, 'motion': 'SWIMMING', 'position': [-4618.752, -742.4]}, {'id': 257, 'motion': 'SWIMMING', 'position': [-4615.424, -740.352]}, {'id': 258, 'motion': 'SWIMMING', 'position': [-4613.632, -738.816]}, {'id': 259, 'motion': 'WALKING', 'position': [-4612.352, -737.024]}, {'id': 260, 'motion': 'SWIMMING', 'position': [-4610.56, -736.0]}, {'id': 261, 'motion': 'WALKING', 'position': [-4609.024, -734.464]}, {'id': 262, 'motion': 'SWIMMING', 'position': [-4607.744, -732.672]}, {'id': 263, 'motion': 'SWIMMING', 'position': [-4606.72, -731.136]}, {'id': 264, 'motion': 'SWIMMING', 'position': [-4605.184, -730.112]}, {'id': 265, 'motion': 'SWIMMING', 'position': [-4603.648, -728.32]}, {'id': 266, 'motion': 'SWIMMING', 'position': [-4602.368, -726.528]}, {'id': 267, 'motion': 'WALKING', 'position': [-4601.344, -725.248]}, {'id': 268, 'motion': 'WALKING', 'position': [-4599.552, -723.456]}, {'id': 269, 'motion': 'SWIMMING', 'position': [-4598.272, -721.664]}, {'id': 270, 'motion': 'SWIMMING', 'position': [-4597.248, -720.128]}, {'id': 271, 'motion': 'SWIMMING', 'position': [-4595.712, -718.592]}, {'id': 272, 'motion': 'SWIMMING', 'position': [-4594.176, -716.544]}, {'id': 273, 'motion': 'WALKING', 'position': [-4592.896, -715.264]}, {'id': 274, 'motion': 'WALKING', 'position': [-4592.128, -713.728]}, {'id': 275, 'motion': 'WALKING', 'position': [-4591.104, -711.68]}, {'id': 276, 'motion': 'WALKING', 'position': [-4589.056, -709.632]}, {'id': 277, 'motion': 'WALKING', 'position': [-4589.056, -709.632]}, {'id': 278, 'motion': 'WALKING', 'position': [-4587.52, -708.864]}, {'id': 279, 'motion': 'WALKING', 'position': [-4587.52, -708.864]}, {'id': 280, 'motion': 'WALKING', 'position': [-4585.984, -707.328]}, {'id': 281, 'motion': 'WALKING', 'position': [-4583.936, -706.048]}, {'id': 282, 'motion': 'WALKING', 'position': [-4583.936, -706.048]}, {'id': 283, 'motion': 'WALKING', 'position': [-4571.392, -699.904]}, {'id': 284, 'motion': 'WALKING', 'position': [-4567.552, -698.112]}, {'id': 285, 'motion': 'WALKING', 'position': [-4563.712, -695.808]}, {'id': 286, 'motion': 'WALKING', 'position': [-4562.176, -695.04]}, {'id': 287, 'motion': 'WALKING', 'position': [-4558.336, -694.272]}, {'id': 288, 'motion': 'WALKING', 'position': [-4556.544, -693.76]}, {'id': 289, 'motion': 'WALKING', 'position': [-4552.192, -691.968]}, {'id': 290, 'motion': 'WALKING', 'position': [-4546.304, -689.664]}, {'id': 291, 'motion': 'WALKING', 'position': [-4540.416, -687.36]}, {'id': 292, 'motion': 'WALKING', 'position': [-4536.32, -685.824]}, {'id': 293, 'motion': 'WALKING', 'position': [-4534.528, -685.056]}, {'id': 294, 'motion': 'WALKING', 'position': [-4528.64, -683.008]}, {'id': 295, 'motion': 'WALKING', 'position': [-4526.592, -681.728]}, {'id': 296, 'motion': 'WALKING', 'position': [-4520.96, -679.68]}, {'id': 297, 'motion': 'WALKING', 'position': [-4516.864, -678.144]}, {'id': 298, 'motion': 'WALKING', 'position': [-4515.328, -677.12]}, {'id': 299, 'motion': 'WALKING', 'position': [-4509.952, -674.816]}, {'id': 300, 'motion': 'WALKING', 'position': [-4507.904, -674.048]}, {'id': 301, 'motion': 'WALKING', 'position': [-4504.064, -672.256]}, {'id': 302, 'motion': 'WALKING', 'position': [-4499.968, -670.208]}, {'id': 303, 'motion': 'WALKING', 'position': [-4497.92, -669.44]}, {'id': 304, 'motion': 'WALKING', 'position': [-4496.128, -668.928]}, {'id': 305, 'motion': 'WALKING', 'position': [-4496.128, -668.928]}, {'id': 306, 'motion': 'SWIMMING', 'position': [-4494.592, -669.696]}, {'id': 307, 'motion': 'SWIMMING', 'position': [-4490.496, -674.304]}, {'id': 308, 'motion': 'SWIMMING', 'position': [-4489.472, -675.584]}, {'id': 309, 'motion': 'SWIMMING', 'position': [-4487.936, -677.12]}, {'id': 310, 'motion': 'SWIMMING', 'position': [-4486.4, -679.168]}, {'id': 311, 'motion': 'SWIMMING', 'position': [-4485.376, -680.192]}, {'id': 312, 'motion': 'SWIMMING', 'position': [-4484.096, -681.984]}, {'id': 313, 'motion': 'SWIMMING', 'position': [-4482.304, -683.776]}, {'id': 314, 'motion': 'SWIMMING', 'position': [-4481.024, -685.056]}, {'id': 315, 'motion': 'SWIMMING', 'position': [-4479.744, -686.336]}, {'id': 316, 'motion': 'SWIMMING', 'position': [-4478.464, -688.384]}, {'id': 317, 'motion': 'SWIMMING', 'position': [-4476.672, -689.664]}, {'id': 318, 'motion': 'SWIMMING', 'position': [-4475.392, -690.944]}, {'id': 319, 'motion': 'SWIMMING', 'position': [-4474.368, -692.992]}, {'id': 320, 'motion': 'SWIMMING', 'position': [-4472.576, -694.528]}, {'id': 321, 'motion': 'SWIMMING', 'position': [-4471.04, -695.552]}, {'id': 322, 'motion': 'SWIMMING', 'position': [-4469.76, -697.088]}, {'id': 323, 'motion': 'SWIMMING', 'position': [-4468.48, -699.136]}, {'id': 324, 'motion': 'SWIMMING', 'position': [-4468.48, -699.136]}, {'id': 325, 'motion': 'SWIMMING', 'position': [-4466.944, -700.416]}, {'id': 326, 'motion': 'SWIMMING', 'position': [-4465.408, -701.952]}, {'id': 327, 'motion': 'SWIMMING', 'position': [-4464.384, -704.0]}, {'id': 328, 'motion': 'SWIMMING', 'position': [-4462.848, -705.28]}, {'id': 329, 'motion': 'SWIMMING', 'position': [-4461.312, -706.304]}, {'id': 330, 'motion': 'SWIMMING', 'position': [-4460.032, -708.096]}, {'id': 331, 'motion': 'SWIMMING', 'position': [-4459.008, -709.888]}, {'id': 332, 'motion': 'WALKING', 'position': [-4457.472, -711.168]}, {'id': 333, 'motion': 'WALKING', 'position': [-4455.936, -712.704]}, {'id': 334, 'motion': 'WALKING', 'position': [-4454.656, -714.24]}, {'id': 335, 'motion': 'WALKING', 'position': [-4454.656, -714.24]}, {'id': 336, 'motion': 'WALKING', 'position': [-4452.608, -713.728]}, {'id': 337, 'motion': 'WALKING', 'position': [-4449.024, -710.912]}, {'id': 338, 'motion': 'WALKING', 'position': [-4443.392, -707.328]}, {'id': 339, 'motion': 'WALKING', 'position': [-4439.552, -705.28]}, {'id': 340, 'motion': 'WALKING', 'position': [-4436.224, -703.232]}, {'id': 341, 'motion': 'WALKING', 'position': [-4432.896, -700.416]}, {'id': 342, 'motion': 'WALKING', 'position': [-4430.592, -699.392]}, {'id': 343, 'motion': 'WALKING', 'position': [-4428.288, -697.088]}, {'id': 344, 'motion': 'WALKING', 'position': [-4424.448, -695.04]}, {'id': 345, 'motion': 'WALKING', 'position': [-4423.168, -694.016]}, {'id': 346, 'motion': 'WALKING', 'position': [-4419.584, -690.432]}, {'id': 347, 'motion': 'WALKING', 'position': [-4414.72, -685.824]}, {'id': 348, 'motion': 'WALKING', 'position': [-4409.6, -681.728]}, {'id': 349, 'motion': 'WALKING', 'position': [-4406.528, -679.424]}, {'id': 350, 'motion': 'WALKING', 'position': [-4404.736, -678.144]}, {'id': 351, 'motion': 'WALKING', 'position': [-4401.664, -674.816]}, {'id': 352, 'motion': 'WALKING', 'position': [-4398.336, -672.512]}, {'id': 353, 'motion': 'WALKING', 'position': [-4393.472, -668.672]}, {'id': 354, 'motion': 'WALKING', 'position': [-4390.4, -665.6]}, {'id': 355, 'motion': 'WALKING', 'position': [-4388.864, -664.576]}, {'id': 356, 'motion': 'SWIMMING', 'position': [-4389.12, -660.48]}, {'id': 357, 'motion': 'SWIMMING', 'position': [-4391.168, -653.056]}, {'id': 358, 'motion': 'SWIMMING', 'position': [-4391.68, -650.496]}, {'id': 359, 'motion': 'SWIMMING', 'position': [-4392.192, -648.704]}, {'id': 360, 'motion': 'SWIMMING', 'position': [-4392.704, -646.912]}, {'id': 361, 'motion': 'SWIMMING', 'position': [-4393.216, -644.608]}, {'id': 362, 'motion': 'SWIMMING', 'position': [-4393.472, -642.816]}, {'id': 363, 'motion': 'SWIMMING', 'position': [-4393.728, -640.512]}, {'id': 364, 'motion': 'WALKING', 'position': [-4393.984, -638.72]}, {'id': 365, 'motion': 'WALKING', 'position': [-4394.496, -636.928]}, {'id': 366, 'motion': 'WALKING', 'position': [-4394.496, -636.928]}, {'id': 367, 'motion': 'WALKING', 'position': [-4392.448, -633.344]}, {'id': 368, 'motion': 'WALKING', 'position': [-4385.536, -627.2]}, {'id': 369, 'motion': 'WALKING', 'position': [-4382.976, -623.872]}, {'id': 370, 'motion': 'WALKING', 'position': [-4380.16, -622.08]}, {'id': 371, 'motion': 'WALKING', 'position': [-4375.808, -617.728]}, {'id': 372, 'motion': 'WALKING', 'position': [-4372.736, -614.144]}, {'id': 373, 'motion': 'WALKING', 'position': [-4369.664, -611.84]}, {'id': 374, 'motion': 'WALKING', 'position': [-4368.128, -610.048]}, {'id': 375, 'motion': 'WALKING', 'position': [-4365.056, -607.488]}, {'id': 376, 'motion': 'WALKING', 'position': [-4359.168, -604.16]}, {'id': 377, 'motion': 'WALKING', 'position': [-4353.024, -602.368]}, {'id': 378, 'motion': 'WALKING', 'position': [-4348.928, -601.088]}, {'id': 379, 'motion': 'WALKING', 'position': [-4344.832, -599.296]}, {'id': 380, 'motion': 'WALKING', 'position': [-4340.992, -598.016]}, {'id': 381, 'motion': 'WALKING', 'position': [-4337.408, -595.712]}, {'id': 382, 'motion': 'WALKING', 'position': [-4333.056, -589.568]}, {'id': 383, 'motion': 'WALKING', 'position': [-4330.752, -587.008]}, {'id': 384, 'motion': 'WALKING', 'position': [-4327.936, -583.168]}, {'id': 385, 'motion': 'WALKING', 'position': [-4325.888, -579.84]}, {'id': 386, 'motion': 'WALKING', 'position': [-4323.072, -577.024]}, {'id': 387, 'motion': 'WALKING', 'position': [-4321.024, -573.184]}, {'id': 388, 'motion': 'WALKING', 'position': [-4317.952, -570.112]}, {'id': 389, 'motion': 'WALKING', 'position': [-4315.904, -567.04]}, {'id': 390, 'motion': 'WALKING', 'position': [-4314.368, -565.248]}, {'id': 391, 'motion': 'WALKING', 'position': [-4311.808, -561.92]}, {'id': 392, 'motion': 'WALKING', 'position': [-4309.248, -558.08]}, {'id': 393, 'motion': 'WALKING', 'position': [-4307.2, -556.288]}, {'id': 394, 'motion': 'WALKING', 'position': [-4305.664, -547.328]}, {'id': 395, 'motion': 'WALKING', 'position': [-4305.152, -544.0]}, {'id': 396, 'motion': 'WALKING', 'position': [-4304.128, -540.16]}, {'id': 397, 'motion': 'WALKING', 'position': [-4302.592, -536.064]}, {'id': 398, 'motion': 'WALKING', 'position': [-4299.264, -533.76]}, {'id': 399, 'motion': 'WALKING', 'position': [-4293.888, -530.432]}, {'id': 400, 'motion': 'WALKING', 'position': [-4290.304, -527.872]}, {'id': 401, 'motion': 'WALKING', 'position': [-4288.512, -526.592]}, {'id': 402, 'motion': 'WALKING', 'position': [-4288.512, -526.592]}, {'id': 403, 'motion': 'WALKING', 'position': [-4286.464, -525.824]}, {'id': 404, 'motion': 'WALKING', 'position': [-4284.672, -525.568]}, {'id': 405, 'motion': 'WALKING', 'position': [-4282.368, -525.568]}, {'id': 406, 'motion': 'WALKING', 'position': [-4278.528, -525.312]}, {'id': 407, 'motion': 'WALKING', 'position': [-4274.432, -526.336]}, {'id': 408, 'motion': 'WALKING', 'position': [-4269.824, -527.616]}, {'id': 409, 'motion': 'WALKING', 'position': [-4264.192, -529.92]}, {'id': 410, 'motion': 'WALKING', 'position': [-4259.84, -530.944]}, {'id': 411, 'motion': 'WALKING', 'position': [-4255.744, -532.224]}, {'id': 412, 'motion': 'WALKING', 'position': [-4251.392, -533.76]}, {'id': 413, 'motion': 'WALKING', 'position': [-4247.552, -535.04]}, {'id': 414, 'motion': 'WALKING', 'position': [-4243.968, -536.064]}, {'id': 415, 'motion': 'WALKING', 'position': [-4239.616, -537.088]}, {'id': 416, 'motion': 'WALKING', 'position': [-4237.824, -537.856]}, {'id': 417, 'motion': 'WALKING', 'position': [-4233.728, -539.648]}, {'id': 418, 'motion': 'WALKING', 'position': [-4229.632, -540.672]}, {'id': 419, 'motion': 'WALKING', 'position': [-4227.84, -541.184]}, {'id': 420, 'motion': 'WALKING', 'position': [-4225.536, -541.44]}, {'id': 421, 'motion': 'WALKING', 'position': [-4224.512, -548.352]}, {'id': 422, 'motion': 'WALKING', 'position': [-4223.232, -555.264]}, {'id': 423, 'motion': 'WALKING', 'position': [-4222.976, -557.056]}, {'id': 424, 'motion': 'WALKING', 'position': [-4222.72, -557.056]}, {'id': 425, 'motion': 'WALKING', 'position': [-4222.464, -559.104]}, {'id': 426, 'motion': 'WALKING', 'position': [-4222.208, -561.664]}, {'id': 427, 'motion': 'WALKING', 'position': [-4221.696, -564.992]}, {'id': 428, 'motion': 'WALKING', 'position': [-4221.44, -567.296]}, {'id': 429, 'motion': 'WALKING', 'position': [-4220.928, -568.832]}, {'id': 430, 'motion': 'WALKING', 'position': [-4220.16, -572.672]}, {'id': 431, 'motion': 'WALKING', 'position': [-4219.648, -574.464]}, {'id': 432, 'motion': 'WALKING', 'position': [-4219.392, -576.768]}, {'id': 433, 'motion': 'FLYING', 'position': [-4219.136, -578.048]}, {'id': 434, 'motion': 'FLYING', 'position': [-4218.624, -582.144]}, {'id': 435, 'motion': 'FLYING', 'position': [-4217.344, -585.984]}, {'id': 436, 'motion': 'FLYING', 'position': [-4216.576, -587.776]}, {'id': 437, 'motion': 'FLYING', 'position': [-4216.064, -589.568]}, {'id': 438, 'motion': 'FLYING', 'position': [-4215.04, -593.152]}, {'id': 439, 'motion': 'FLYING', 'position': [-4214.016, -597.504]}, {'id': 440, 'motion': 'FLYING', 'position': [-4212.992, -601.088]}, {'id': 441, 'motion': 'FLYING', 'position': [-4212.224, -602.88]}, {'id': 442, 'motion': 'FLYING', 'position': [-4210.432, -606.976]}, {'id': 443, 'motion': 'FLYING', 'position': [-4208.896, -610.304]}, {'id': 444, 'motion': 'FLYING', 'position': [-4208.384, -612.608]}, {'id': 445, 'motion': 'FLYING', 'position': [-4205.568, -615.68]}, {'id': 446, 'motion': 'FLYING', 'position': [-4203.52, -618.752]}, {'id': 447, 'motion': 'FLYING', 'position': [-4202.24, -620.032]}, {'id': 448, 'motion': 'FLYING', 'position': [-4199.168, -623.104]}, {'id': 449, 'motion': 'FLYING', 'position': [-4195.584, -625.408]}, {'id': 450, 'motion': 'FLYING', 'position': [-4195.84, -625.408]}, {'id': 451, 'motion': 'FLYING', 'position': [-4194.304, -626.176]}, {'id': 452, 'motion': 'FLYING', 'position': [-4194.304, -626.176]}, {'id': 453, 'motion': 'FLYING', 'position': [-4194.816, -628.224]}, {'id': 454, 'motion': 'FLYING', 'position': [-4194.816, -627.968]}, {'id': 455, 'motion': 'FLYING', 'position': [-4195.84, -628.992]}, {'id': 456, 'motion': 'FLYING', 'position': [-4197.632, -630.272]}, {'id': 457, 'motion': 'FLYING', 'position': [-4198.912, -632.064]}, {'id': 458, 'motion': 'FLYING', 'position': [-4201.728, -634.368]}, {'id': 459, 'motion': 'FLYING', 'position': [-4203.52, -636.16]}, {'id': 460, 'motion': 'FLYING', 'position': [-4206.08, -638.976]}, {'id': 461, 'motion': 'FLYING', 'position': [-4207.872, -640.0]}, {'id': 462, 'motion': 'FLYING', 'position': [-4210.432, -643.072]}, {'id': 463, 'motion': 'FLYING', 'position': [-4211.968, -644.352]}, {'id': 464, 'motion': 'FLYING', 'position': [-4213.504, -645.632]}, {'id': 465, 'motion': 'FLYING', 'position': [-4213.504, -645.632]}, {'id': 466, 'motion': 'WALKING', 'position': [-4212.224, -640.256]}, {'id': 467, 'motion': 'WALKING', 'position': [-4212.224, -640.256]}, {'id': 468, 'motion': 'WALKING', 'position': [-4210.944, -636.672]}, {'id': 469, 'motion': 'WALKING', 'position': [-4210.176, -634.368]}, {'id': 470, 'motion': 'WALKING', 'position': [-4208.64, -630.528]}, {'id': 471, 'motion': 'WALKING', 'position': [-4207.616, -628.736]}, {'id': 472, 'motion': 'WALKING', 'position': [-4206.336, -627.456]}, {'id': 473, 'motion': 'WALKING', 'position': [-4204.288, -623.36]}, {'id': 474, 'motion': 'WALKING', 'position': [-4203.776, -621.568]}, {'id': 475, 'motion': 'WALKING', 'position': [-4202.752, -619.264]}, {'id': 476, 'motion': 'WALKING', 'position': [-4200.96, -615.936]}, {'id': 477, 'motion': 'WALKING', 'position': [-4199.68, -613.632]}, {'id': 478, 'motion': 'WALKING', 'position': [-4198.656, -612.608]}, {'id': 479, 'motion': 'WALKING', 'position': [-4198.656, -612.608]}, {'id': 480, 'motion': 'WALKING', 'position': [-4196.864, -611.84]}, {'id': 481, 'motion': 'WALKING', 'position': [-4180.992, -612.608]}, {'id': 482, 'motion': 'WALKING', 'position': [-4177.152, -612.864]}, {'id': 483, 'motion': 'WALKING', 'position': [-4172.544, -613.376]}, {'id': 484, 'motion': 'WALKING', 'position': [-4169.984, -613.376]}, {'id': 485, 'motion': 'WALKING', 'position': [-4165.888, -613.888]}, {'id': 486, 'motion': 'WALKING', 'position': [-4161.792, -614.4]}, {'id': 487, 'motion': 'WALKING', 'position': [-4157.44, -615.168]}, {'id': 488, 'motion': 'WALKING', 'position': [-4153.088, -615.68]}, {'id': 489, 'motion': 'WALKING', 'position': [-4151.04, -616.192]}, {'id': 490, 'motion': 'WALKING', 'position': [-4146.688, -616.96]}, {'id': 491, 'motion': 'WALKING', 'position': [-4144.64, -617.728]}, {'id': 492, 'motion': 'WALKING', 'position': [-4142.848, -618.752]}, {'id': 493, 'motion': 'WALKING', 'position': [-4139.008, -623.872]}, {'id': 494, 'motion': 'WALKING', 'position': [-4134.4, -631.808]}, {'id': 495, 'motion': 'WALKING', 'position': [-4132.864, -633.344]}, {'id': 496, 'motion': 'WALKING', 'position': [-4130.816, -637.44]}, {'id': 497, 'motion': 'WALKING', 'position': [-4127.744, -640.512]}, {'id': 498, 'motion': 'WALKING', 'position': [-4125.696, -644.352]}, {'id': 499, 'motion': 'WALKING', 'position': [-4122.88, -647.936]}, {'id': 500, 'motion': 'WALKING', 'position': [-4122.88, -647.936]}, {'id': 501, 'motion': 'WALKING', 'position': [-4120.576, -651.008]}, {'id': 502, 'motion': 'WALKING', 'position': [-4116.224, -655.616]}, {'id': 503, 'motion': 'WALKING', 'position': [-4114.176, -659.456]}, {'id': 504, 'motion': 'WALKING', 'position': [-4111.616, -663.04]}, {'id': 505, 'motion': 'WALKING', 'position': [-4110.848, -664.32]}, {'id': 506, 'motion': 'WALKING', 'position': [-4110.848, -664.32]}], 'break_position': [[-4274.432, -952.32], [-4280.064, -950.272], [-4290.56, -941.568], [-4304.128, -934.4], [-4324.096, -930.816], [-4378.88, -940.288], [-4411.392, -951.296], [-4434.432, -926.464], [-4459.008, -896.256], [-4492.08, -903.4019999999999], [-4524.288, -905.984], [-4564.168000000001, -912.28], [-4577.536, -888.32], [-4652.004000000001, -827.7259999999999], [-4659.968, -826.624], [-4704.0, -827.136], [-4761.856, -822.272], [-4800.264, -787.6999999999999], [-4737.28, -762.624], [-4666.822, -774.3019999999999], [-4658.944, -768.0], [-4618.608, -743.4639999999999], [-4587.828, -709.6859999999999], [-4562.176, -695.04], [-4498.39, -671.5939999999999], [-4453.636, -715.5899999999999], [-4423.168, -694.016], [-4388.158, -665.716], [-4393.926, -637.76], [-4359.168, -604.16], [-4337.408, -595.712], [-4307.2, -556.288], [-4302.592, -536.064], [-4286.464, -525.824], [-4278.528, -525.312], [-4225.536, -541.44], [-4218.624, -582.144], [-4212.224, -602.88], [-4199.182000000001, -612.702], [-4205.568, -615.68], [-4194.304, -626.432], [-4212.808, -644.814], [-4210.944, -636.672], [-4199.68, -613.632], [-4177.152, -612.864], [-4146.688, -616.96], [-4139.008, -623.872], [-4110.848, -664.32]], 'time': '', 'additional_info': {'path_recorder': '1.0', 'manually_modified': 'true'}, 'adsorptive_position': [[-4564.17, -912.28], [-4587.83, -709.69], [-4498.39, -671.59], [-4388.16, -665.72], [-4212.81, -644.81], [-4199.18, -612.7]], 'generate_from': 'path recorder 1.0'}

META={'name': {'zh_CN': '月莲-须弥护世森13个'}, 'author': 'GIA', 'tags': {'zh_CN': ['采集'], 'en_US': ['Collect']}, 'local_edit_mission': '月莲-须弥护世森13个', 'description': '', 'note': ''}

class MissionMain(MissionJustCollect):
    def __init__(self):
        super().__init__(tlp2m_default_value, "tlp2m_default_name",)

if __name__ == '__main__':
    mission = MissionMain()
    mission.start()
