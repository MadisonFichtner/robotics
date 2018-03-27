package com.madplant.tango;

import android.speech.tts.TextToSpeech;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.net.Socket;

public class Client extends Thread implements Runnable{
    private Socket socket;
    private PrintWriter out = null;
    private BufferedReader in = null;
    private String message = null;

    TextToSpeech t1;

    public Client(TextToSpeech t1) {
        this.t1 = t1;
    }

    @Override
    public void run() {
        try {
            socket = new Socket("192.168.0.165", 1000);
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

    public void speak(String message) {
        t1.speak(message, TextToSpeech.QUEUE_FLUSH, null);
    }

    public void write(String message) {
        this.message = message;
    }

    public void disconnect() {
        try {
            socket.close();
            in.close();
            out.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    class ReadThread extends Thread implements Runnable{
        boolean done = false;

        @Override
        public void run() {
            while(!done) {
                try {
                    String message = in.readLine();
                    System.out.println(message);
                    speak(message);
                } catch (Exception e) {
                    e.printStackTrace();
                    done = true;
                }
            }
            disconnect();
        }
    }
}
