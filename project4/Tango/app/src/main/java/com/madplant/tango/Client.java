package com.madplant.tango;

import android.speech.tts.TextToSpeech;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.net.Socket;

public class Client extends Thread{
    private Socket socket;
    private PrintWriter out = null;
    private BufferedReader in = null;
    private String message = null;
    private MainActivity activity;

    private TextToSpeech t1;

    Client(TextToSpeech t1, MainActivity activity) {
        this.t1 = t1;
        this.activity = activity;
    }

    //thread for writing to network
    @Override
    public void run() {
        try {
            socket = new Socket("10.200.49.223", 2000);
            out = new PrintWriter(socket.getOutputStream());
            in = new BufferedReader(new InputStreamReader(socket.getInputStream()));
            ReadThread readThread = new ReadThread();
            readThread.start();
        } catch (Exception e) {
            e.printStackTrace();
        }

        boolean done = false;

        while (!done) {
            if (message != null) {
                try {
                    out.print(message);
                    out.flush();
                    message = null;
                } catch (Exception e) {
                    e.printStackTrace();
                    try {
                        socket.close();
                        in.close();
                        out.close();
                        done = true;
                    } catch (IOException d) {
                        e.printStackTrace();
                    }
                }
            }
        }
        disconnect();
    }

    // text to speech
    private void speak(String message) {
        t1.speak(message, TextToSpeech.QUEUE_FLUSH, null);
    }

    // set message to send to pi
    void write(String message) {
        this.message = message;
    }

    // disconnect from server
    private void disconnect() {
        try {
            socket.close();
            in.close();
            out.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    //thread for reading from network
    class ReadThread extends Thread {
        boolean done = false;

        @Override
        public void run() {
            while(!done) {
                try {
                    String message = in.readLine();
                    System.out.println(message);
                    //start voice recognition if the message is "%listen"
                    if(message.equals("%listen")) {
                        activity.startVoiceRecognitionActivity();
                    }
                    //otherwise just speak the message
                    else {
                        speak(message);
                    }
                } catch (Exception e) {
                    e.printStackTrace();
                    done = true;
                }
            }
            disconnect();
        }
    }
}
