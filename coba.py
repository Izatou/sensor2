from index import CMD2_PREDICT, bootstrap
import pandas as pd

def main():
    boot = bootstrap()

    # For example, we take the data from csv
    allData = pd.read_csv("/home/pi/LCD_SPI_INOSE/N_101018_11074.csv",sep=";")

    #allData = allData[allData['sampling_id'] == 740]

    # Convert them to dataframe
    # with header 'MQ2_ADC', 'MQ3_ADC', 'MQ4_ADC', 'TGS2610_ADC', 'TGS2600_ADC', 'TGS822_ADC', 'MQ137_ADC', 'MQ138_ADC'
    allData = allData.loc[:,['PROCESS', 'MQ2_ADC', 'MQ3_ADC', 'MQ4_ADC', 'TGS2610_ADC', 'TGS2600_ADC', 'TGS822_ADC', 'MQ137_ADC', 'MQ138_ADC']]    

    # Split the PROCESS
    (valid, covid) = CMD2_PREDICT(
        boot, 
        allData[allData['PROCESS'] == 'P1'],
        allData[allData['PROCESS'] == 'P2'],
        allData[allData['PROCESS'] == 'P3'],
    )

    print(valid, covid)


if __name__ == "__main__":
    main()
