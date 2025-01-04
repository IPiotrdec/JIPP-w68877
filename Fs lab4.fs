//zad3
open System

let analizaTekstu (tekst: string) : int * int * string =
    let slowa : string array = tekst.Split([|' '; '\t'; '\n'; '\r'|], StringSplitOptions.RemoveEmptyEntries)
    let liczbaSlow : int = slowa.Length
    let liczbaZnakow : int = slowa |> Array.sumBy (fun s -> s.Length)
    let slowaCzestotliwosc : (string * int) list = 
        slowa
        |> Seq.groupBy id
        |> Seq.map (fun (word, group) -> word, Seq.length group)
        |> Seq.sortByDescending snd
        |> Seq.toList
    let najczestsze : string = 
        match slowaCzestotliwosc with
        | (word, _) :: _ -> word
        | [] -> "Brak danych"
    liczbaSlow, liczbaZnakow, najczestsze

printfn "Podaj tekst do analizy:"
let tekst : string = Console.ReadLine()

let liczbaSlow, liczbaZnakow, najczestsze = analizaTekstu tekst
printfn "Liczba słów: %d" liczbaSlow
printfn "Liczba znaków (bez spacji): %d" liczbaZnakow
printfn "Najczęściej występujące słowo: %s" najczestsze

//zad2
open System

// Mapowanie kursów walut
let kursyWalut = 
    Map.ofList [
        ("USD", 4.0)  // Przykładowy kurs dla USD
        ("EUR", 4.5)  // Przykładowy kurs dla EUR
        ("GBP", 5.2)  // Przykładowy kurs dla GBP
    ]

// Funkcja do przeliczania kwoty
let przeliczKwote (kwota: float) (walutaZ: string) (walutaNa: string) : float option =
    if Map.containsKey walutaZ kursyWalut && Map.containsKey walutaNa kursyWalut then
        let kursZ = kursyWalut.[walutaZ]
        let kursNa = kursyWalut.[walutaNa]
        Some (kwota * kursNa / kursZ)
    else
        None

// Pobranie danych od użytkownika
printfn "Podaj kwotę do przeliczenia: "
let kwota = Console.ReadLine() |> float

printfn "Podaj walutę źródłową (np. USD, EUR, GBP): "
let walutaZ = Console.ReadLine()

printfn "Podaj walutę docelową (np. USD, EUR, GBP): "
let walutaNa = Console.ReadLine()

// Przeliczenie kwoty i wyświetlenie wyniku
match przeliczKwote kwota walutaZ walutaNa with
| Some wynik -> printfn "Przeliczona kwota: %.2f %s" wynik walutaNa
| None -> printfn "Podano nieprawidłowe waluty. Spróbuj ponownie."

//zad1

open System

// Funkcja do obliczania BMI i określania kategorii
let obliczBMI (masa: float) (wzrost: float) : float * string =
    let bmi = masa / (wzrost / 100.0) ** 2.0
    let kategoria =
        if bmi < 18.5 then "Niedowaga"
        elif bmi < 25.0 then "Waga prawidłowa"
        elif bmi < 30.0 then "Nadwaga"
        else "Otyłość"
    bmi, kategoria

// Pobranie danych od użytkownika
printfn "Podaj swoją wagę (kg): "
let masa = Console.ReadLine() |> float

printfn "Podaj swój wzrost (cm): "
let wzrost = Console.ReadLine() |> float

// Obliczenie BMI i wyświetlenie wyników
let bmi, kategoria = obliczBMI masa wzrost
printfn "Twoje BMI: %.2f" bmi
printfn "Kategoria BMI: %s" kategoria


