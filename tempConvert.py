def temperatureConverter(degree,type):
    if(type == 'F'):
        Cel = (degree - 32)*5/9
        print(f'Celsius value: {Cel=}')

    if(type == 'C'):
        Fah = (degree * 9/5) + 32
        print(f'Fahrenheit value:  {Fah=}')


temperatureConverter(0,'F')
temperatureConverter(100,'C')