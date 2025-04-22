import bilby
from bilby.gw.source import lal_binary_black_hole
from bilby.gw.conversion import convert_to_lal_binary_black_hole_parameters
#create bilby waveform generator
def WaveformGenerator(duration, sampling_frequency, start_time):
    waveform_arguments = {
        'waveform_approximate': 'IMRPhenomXP',
        'refrence_frequency': 100.0,
        'catch_waveform_error': True,
    }
    #parameters^^
    #conversion
    g = bilby.gw.waveform_generator.WaveformGenerator(
        duration = duration,
        sampling_frequency=sampling_frequency,
        start_time=start_time,
        frequency_domain_source_model=lal_binary_black_hole,
        parameter_conversion=convert_to_lal_binary_black_hole_parameters,
        waveform_arguments=waveform_arguments,
    )
    #additional attributes
    g.duration = duration
    g.sampling_frequency = sampling_frequency
    g.start_time = start_time

    return g