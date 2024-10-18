const mqtt = require('mqtt');

// MQTT broker details
const brokerUrl = 'mqtt://192.168.1.19';
const topic = 'temperature/topic';

// Connect to the MQTT broker
const client = mqtt.connect(brokerUrl);

client.on('connect', () => {
  console.log('Connected to MQTT broker');
  client.subscribe(topic, (err) => {
    if (err) {
      console.error('Failed to subscribe to topic:', err);
    } else {
      console.log('Subscribed to topic:', topic);
    }
  });
});

client.on('message', (topic, message) => {
  console.log(`Received message on topic ${topic}: ${message.toString()}`);
});

client.on('error', (err) => {
  console.error('MQTT error:', err);
});