import bilby

from gwpy.timeseries import TimeSeries
from bilby.gw.detector import Interferometer as BilbyInterferometer
from bilby.gw.detector import PowerSpectralDensity

def Interferometer(name, time_of_event, post_trigger_duration = 2, duration = 4, sample_rate = 4096, maximum_frequency = 1020):

    #load strain data
    start_time = time_of_event + post_trigger_duration
    end_time = start_time + duration


    strain = TimeSeries.fetch_open_data(name, start_time, end_time, smaple_rate = sample_rate)

    strain = strain.crop(start_time + 0.5, end_time - 0.5)
    strain = strain.highpass_fir(15, 512)
    #estimate psd
    psd = strain.psd(fftlength = 4)
    psd = psd.interpolate(strain.frequency)
    psd = psd.crop(20, maximum_frequency)
    #create interferometer with bilby
    interferometer = BilbyInterferometer(name)
    interferometer.set_strain_data_from_gwpy_timeseries(strain, sample_rate = sample_rate, duration=duration, start_time = start_time)
    interferometer.power_spectral_density = PowerSpectralDensity(frequency_array = psd.frequences.value, psd_array = psd.value)

    return interferometer
