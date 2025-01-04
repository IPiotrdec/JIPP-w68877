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
