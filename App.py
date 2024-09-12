import java.util.Random;

// Mock sensor class
class IoTSensor {
    private String sensorType;
    private Random random;

    public IoTSensor(String type) {
        this.sensorType = type;
        this.random = new Random();
    }

    // Simulate sensor data reading
    public double readData() {
        switch (sensorType) {
            case "Temperature":
                return 15 + (40 - 15) * random.nextDouble(); // Random temperature between 15 and 40°C
            case "SoilMoisture":
                return random.nextInt(100); // Random soil moisture percentage
            case "Humidity":
                return 30 + (90 - 30) * random.nextDouble(); // Random humidity between 30% and 90%
            default:
                return 0;
        }
    }
}

// Main class
public class PrecisionAgriculture {

    public static void main(String[] args) {
        // Creating sensor instances
        IoTSensor tempSensor = new IoTSensor("Temperature");
        IoTSensor moistureSensor = new IoTSensor("SoilMoisture");
        IoTSensor humiditySensor = new IoTSensor("Humidity");

        // Simulate data readings
        double temperature = tempSensor.readData();
        double moisture = moistureSensor.readData();
        double humidity = humiditySensor.readData();

        // Simulate data transmission to a server
        sendDataToServer("Temperature", temperature);
        sendDataToServer("SoilMoisture", moisture);
        sendDataToServer("Humidity", humidity);
    }

    // Simulated method for sending data to a server
    public static void sendDataToServer(String sensorType, double value) {
        System.out.println("Sending data: " + sensorType + " - " + value);
        // You can use HTTP client libraries like HttpClient or MQTT for real implementation
    }
}
