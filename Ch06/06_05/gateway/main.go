package main

import (
	"context"
	"log"
	"net/http"
	"os"

	"github.com/grpc-ecosystem/grpc-gateway/v2/runtime"
	"google.golang.org/grpc"

	"gateway/pb"
)

func main() {
	ridesHost := os.Getenv("RIDES_HOST")
	if ridesHost == "" {
		ridesHost = "localhost:8888"
	}

	ctx := context.Background()
	mux := runtime.NewServeMux()
	opts := []grpc.DialOption{grpc.WithInsecure()}
	if err := pb.RegisterRidesHandlerFromEndpoint(ctx, mux, ridesHost, opts); err != nil {
		log.Fatal(err)
	}

	addr := ":8080"
	log.Printf("gateway server ready on %s", addr)

	if err := http.ListenAndServe(addr, mux); err != nil {
		log.Fatal(err)
	}
}
