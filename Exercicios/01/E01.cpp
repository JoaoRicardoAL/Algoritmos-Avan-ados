#include <iostream>
#include <map>
#include <string>

using namespace std;

typedef struct
{
    int id_pai;
    int id_mae;
    bool diabetes;
} Pessoa;

bool diabete_herdada(int id, map<int, Pessoa> arvore)
{
    if (id == -1)
        return false;
    if (arvore[id].id_mae == -1 && arvore[id].id_pai == -1)
        return false;
    else
        return (arvore[id].diabetes && (arvore[arvore[id].id_mae].diabetes || arvore[arvore[id].id_pai].diabetes));
}

int main()
{

    int entrada;
    cin >> entrada;

    for (int i = 0; i < entrada; i++)
    {
        int num_pessoas;
        cin >> num_pessoas;
        map<int, Pessoa> arvore;

        for (int j = 0; j < num_pessoas; j++)
        {
            int id, id_pai, id_mae;
            string diabetes;
            cin >> id >> diabetes >> id_pai >> id_mae;
            if (diabetes == "sim")
                arvore[id] = {id_pai, id_mae, true};
            else
                arvore[id] = {id_pai, id_mae, false};
        }
        int contador_diabetes = 0;
        for (int id = 0; id < num_pessoas; id++)
        {
            if (diabete_herdada(id, arvore))
            {
                contador_diabetes++;
            }
        }
        cout << contador_diabetes << endl;
    }

    return 0;
}