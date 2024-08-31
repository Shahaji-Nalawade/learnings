package main

import (
	"encoding/json"
	"fmt"
	"net/http"
)

var groceries = []Grocery{
    {Name: "Almod Milk", Quantity: 2},
    {Name: "Apple", Quantity: 6},
}

func AllGroceries(w http.ResponseWriter, r *http.Request) {

    fmt.Println("Endpoint hit: returnAllGroceries")
    json.NewEncoder(w).Encode(groceries)
}