package main

import (
	"fmt"
	"log"
	"net/http"

	"github.com/gorilla/mux"
)
func main() {

    r := mux.NewRouter().StrictSlash(true)
    r.HandleFunc("/allgroceries", hello) // ----> To request all groceries
    // r.HandleFunc("/groceries/{name}", SingleGrocery) // ----> To request a specific grocery
    // r.HandleFunc("/groceries", GroceriesToBuy).Methods("POST") // ----> To add  new grocery to buy
    // r.HandleFunc("/groceries/{name}", UpdateGrocery).Methods("PUT")// ----> To update a grocery
    // r.HandleFunc("/groceries/{name}", DeleteGrocery).Methods("DELETE") // ----> Delete a grocery
    fmt.Println("test")
    log.Fatal(http.ListenAndServe(":10000", r))

}


func hello(http.ResponseWriter, *http.Request){
    fmt.Println("Hello world")
}