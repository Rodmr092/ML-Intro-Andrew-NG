import numpy as np
import soundfile as sf

# Load a noise sample (replace 'path_to_noise.wav' with your actual file path)
noise, sampling_rate = sf.read('white_noise.wav')

# Invert the phase of the noise
inverse_noise = -noise

# Save the inverse noise to a new file
sf.write('inverse_noise.wav', inverse_noise, sampling_rate)

