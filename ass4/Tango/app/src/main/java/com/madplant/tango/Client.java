package com.madplant.tango;

import java.net.Socket;

public class Client extends Thread implements Runnable {
    @Override
    public void run() {
        try {
            Socket s = new Socket("10.200.48.152", 8080);
            s.getOutputStream().write("bye".getBytes());
            s.close();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
