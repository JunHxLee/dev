package main

import (
    "fmt"
    "net"
    "bufio"
)

func main() {
    ln, err := net.Listen("tcp", ":8080")
    if err != nil {
        fmt.Println("Error starting server:", err)
        return
    }
    defer ln.Close()
    fmt.Println("Server is listening on port 8080...")

    for {
        conn, err := ln.Accept()
        if err != nil {
            fmt.Println("Connection error:", err)
            continue
        }
        go handleConnection(conn)
    }
}

func handleConnection(conn net.Conn) {
    defer conn.Close()
    fmt.Println("Client connected:", conn.RemoteAddr())
    
    reader := bufio.NewReader(conn)
    for {
        message, err := reader.ReadString('\n')
        if err != nil {
            fmt.Println("Client disconnected:", conn.RemoteAddr())
            return
        }
        fmt.Print("Received from client: ", message)
        conn.Write([]byte("Echo: " + message))
    }
}
