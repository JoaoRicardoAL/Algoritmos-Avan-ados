#include <iostream>
#include <unordered_map>
#include <string>
#include <iomanip>

using namespace std;

int main()
{
    // Recebe o número de cadastros a serem feitos
    int cadastros = 0;
    cin >> cadastros;

    // Utiliza um mapa para armazenar o estoque de produtos de forma única
    unordered_map<string, float> estoque;
    for (int i = 0; i < cadastros; i++)
    {
        // Recebe o código e o preço por kilo do produto
        string codigo;
        float preco;
        cin >> codigo >> preco;

        if (estoque.find(codigo) != estoque.end())
        {
            cout << "Produto com código " << codigo << " já cadastrado." << endl;
        }
        else
        {
            estoque[codigo] = preco;
        }
    }

    // Recebe o número de compras a serem feitas
    int compras = 0;
    while (true)
    {
        cin >> compras;
        if (compras < 0)
            break;

        // Recebe o código e o peso dos produtos a serem comprados, verifica se estão no estoque e calcula o preço total
        string codigo;
        float peso;
        float total = 0.0f;
        for (int i = 0; i < compras; i++)
        {
            cin >> codigo >> peso;
            if (estoque.find(codigo) == estoque.end())
            {
                cout << "Produto com código " << codigo << " não cadastrado." << endl;
            }
            else
            {
                total += estoque[codigo] * peso;
            }
        }
        cout << "R$" << fixed << setprecision(2) << total << endl;
    }
    return 0;
}