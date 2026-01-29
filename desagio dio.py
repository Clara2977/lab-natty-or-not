def gerar_projeto_gastronomico():
    print("--- 📒 GERADOR DE CARDÁPIO ZERO LACTOSE ---")
    
    # Dicionário com os dados das receitas
    receitas = {
        "1": {
            "nome": "Risoto de Funghi (Zero Lactose)",
            "ingrediente_chave": "Arroz Arbóreo e Leite de Castanhas",
            "prompt": "Extreme close-up of a gourmet creamy mushroom risotto, dairy-free, steam rising, macro photography, natural lighting."
        },
        "2": {
            "nome": "Lasanha de 'Queijo' de Castanhas",
            "ingrediente_chave": "Leite de Amêndoas e Polvilho",
            "prompt": "Lasanha with bubbling dairy-free cheese, golden crust, messy edges, cinematic lighting, hyper-realistic."
        },
        "3": {
            "nome": "Cheesecake de Frutas Vermelhas",
            "ingrediente_chave": "Creme de Coco e Tofu Macio",
            "prompt": "Slice of strawberry cheesecake, coconut cream, glossy red berry sauce, realistic textures, high-end restaurant style."
        }
    }

    print("\nEscolha uma receita para ver os detalhes e o prompt da IA:")
    for id, dados in receitas.items():
        print(f"{id}. {dados['nome']}")

    escolha = input("\nDigite o número da receita: ")

    if escolha in receitas:
        r = receitas[escolha]
        print(f"\n--- ✨ RESULTADO PARA O PROJETO ---")
        print(f"📌 Título: {r['nome']}")
        print(f"🥛 Substituto de Lactose: {r['ingrediente_chave']}")
        print(f"🤖 Prompt para a IA de Imagem: \n   {r['prompt']}")
        print("-" * 35)
    else:
        print("Opção inválida! Tente de 1 a 3.")

# Executa a função
gerar_projeto_gastronomico()
