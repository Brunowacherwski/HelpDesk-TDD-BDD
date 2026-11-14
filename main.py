from src.service import ChamadoService


def menu():
    service = ChamadoService()

    while True:
        print("\n=== SISTEMA DE HELP DESK ===")
        print("1. Abrir chamado")
        print("2. Buscar chamado por ID")
        print("3. Encerrar chamado")
        print("4. Reabrir chamado")
        
        print("0. Sair")

        opcao = input("Escolha uma opção: ").strip()

        try:
            if opcao == "1":
                titulo = input("Título: ")
                desc = input("Descrição: ")
                print(f"Prioridades disponíveis: {service.listar_prioridades()}")
                prio = input("Prioridade (Enter para Media): ").strip().capitalize() or "Media"
                c = service.abrir_chamado(titulo, desc, prio)
                print(f"Chamado #{c.id} aberto com sucesso!")

            elif opcao == "2":
                cid = int(input("ID do chamado: "))
                print(service.buscar_chamado(cid))
            elif opcao == "3":
                cid = int(input("ID do chamado: "))
                solucao = input("Solução aplicada: ")
                c = service.encerrar_chamado(cid, solucao)
                print(f"Chamado #{c.id} encerrado em {c.data_encerramento:%d/%m/%Y %H:%M}.")

            elif opcao == "4":
                cid = int(input("ID do chamado: "))
                c = service.reabrir_chamado(cid)
                print(f"Chamado #{c.id} reaberto com status {c.status}.")

            elif opcao == "0":
                print("Saindo...")
                break
            else:
                print("Opção inválida.")
        except ValueError as erro:
            print(f"Erro: {erro}")


if __name__ == "__main__":
    menu()