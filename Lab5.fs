open System

// Zadanie 1: Rekurencyjne generowanie ciągu Fibonacciego
let rec fibonacci n =
    if n <= 1 then n
    else fibonacci (n - 1) + fibonacci (n - 2)

let fibonacciTail n =
    let rec aux n a b =
        if n = 0 then a
        elif n = 1 then b
        else aux (n - 1) b (a + b)
    aux n 0 1

// Zadanie 2: Wyszukiwanie elementu w drzewie binarnym
type Tree<'T> =
    | Empty
    | Node of 'T * Tree<'T> * Tree<'T>

let rec searchTree value tree =
    match tree with
    | Empty -> false
    | Node(v, left, right) ->
        if v = value then true
        elif value < v then searchTree value left
        else searchTree value right

let searchTreeIter value tree =
    let rec aux stack =
        match stack with
        | [] -> false
        | Empty :: rest -> aux rest
        | Node(v, left, right) :: rest ->
            if v = value then true
            else aux (left :: right :: rest)
    aux [tree]

// Zadanie 3: Generowanie permutacji listy
let rec permutations list =
    match list with
    | [] -> [[]]
    | x :: xs ->
        permutations xs
        |> List.collect (fun perm -> [for i in 0 .. List.length perm -> List.insertAt i x perm])

// Zadanie 4: Problem wież Hanoi
let rec hanoi n source target auxiliary =
    if n > 0 then
        hanoi (n - 1) source auxiliary target
        printfn "Przenieś dysk z %s do %s" source target
        hanoi (n - 1) auxiliary target source

let hanoiIter n source target auxiliary =
    printfn "Iteracyjna wersja wież Hanoi "

// Zadanie 5: Implementacja QuickSort
let rec quicksort list =
    match list with
    | [] -> []
    | pivot :: rest ->
        let smaller = List.filter ((>=) pivot) rest
        let greater = List.filter ((<) pivot) rest
        quicksort smaller @ [pivot] @ quicksort greater

let quicksortIter list =
    printfn "Iteracyjna wersja QuickSort"
