import tkinter as tk
from tkinter import messagebox

class Escolha:
    def _init_(self, texto, impacto, resultado):
        self.texto = texto
        self.impacto = impacto
        self.resultado = resultado

class Missao:
    def _init_(self, titulo, narrativa, escolhas):
        self.titulo = titulo
        self.narrativa = narrativa
        self.escolhas = escolhas

class JogoGUI:
    def _init_(self, root):
        self.root = root
        self.root.title("🌱 ECOGÊNESE: O LEGADO DO DOUTOR 🌍")
        self.nome_jogador = ""
        self.pontuacao = {'ecologico': 0, 'social': 0, 'tecnologico': 0, 'sustentavel': 0}
        self.missoes = self.criar_missoes()
        self.missao_atual = 0
        self.tela_inicial()

    def tela_inicial(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        titulo = tk.Label(self.root, text="🌱 ECOGÊNESE: O LEGADO DO DOUTOR 🌍", font=("Helvetica", 20, "bold"), fg="green")
        titulo.pack(pady=20)

        historia = "Em um planeta à beira do colapso ambiental, você é a última esperança. Como um brilhante cientista em biotecnologia ambiental, foi recrutado pelo Projeto Ecogênese. Sua missão: usar ciência e sabedoria para salvar ecossistemas devastados. As escolhas são suas. O destino do mundo está em suas mãos."
        descricao = tk.Label(self.root, text=historia, wraplength=600, justify="center", font=("Helvetica", 12))
        descricao.pack(pady=20)

        rotulo_nome = tk.Label(self.root, text="Digite o nome do personagem:", font=("Helvetica", 12))
        rotulo_nome.pack()
        self.entrada_nome = tk.Entry(self.root, font=("Helvetica", 12))
        self.entrada_nome.pack(pady=10)

        botao_jogar = tk.Button(self.root, text="Iniciar Jogo", font=("Helvetica", 12, "bold"), command=self.iniciar_jogo)
        botao_jogar.pack(pady=20)

    def iniciar_jogo(self):
        nome_digitado = self.entrada_nome.get()
        if nome_digitado.strip():
            self.nome_jogador = nome_digitado.strip()
            self.exibir_missao()
        else:
            messagebox.showwarning("Atenção", "Por favor, digite o nome do personagem.")

    def criar_missoes(self):
        return [
            Missao(
                "Missão 1: A Cidade Envenenada",
                "Uma metrópole foi contaminada por metais pesados. Como você, Dr(a). {}, irá agir para descontaminar o solo?".format(self.nome_jogador),
                [
                    Escolha("Usar MGMs para metabolizar os metais", {'ecologico': -2, 'tecnologico': 2}, "Os MGMs funcionaram, mas causaram mutações em insetos locais. A mídia critica sua decisão."),
                    Escolha("Usar plantas hiperacumuladoras", {'ecologico': 2, 'sustentavel': 2}, "As plantas começaram a absorver lentamente os metais. A população aplaude sua paciência e sabedoria."),
                    Escolha("Ignorar protocolos e usar agentes químicos", {'ecologico': -5}, "O solo entrou em combustão! Uma explosão causou caos e poluição aérea."),
                ]
            ),
            Missao(
                "Missão 2: A Floresta Esquecida",
                "Uma floresta tropical devastada por queimadas precisa ser restaurada. Dr(a). {}, qual caminho seguirá?".format(self.nome_jogador),
                [
                    Escolha("Implantar sementes bioengenheiradas", {'tecnologico': 2, 'sustentavel': -1}, "As árvores crescem rápido, mas algumas espécies dominam e sufocam outras."),
                    Escolha("Reflorestamento com comunidades locais", {'social': 3, 'ecologico': 2}, "As comunidades se unem e a floresta começa a renascer naturalmente."),
                    Escolha("Pulverizar aceleradores genéticos por drones", {'ecologico': -4}, "Uma reação em cadeia de crescimento descontrolado destrói biomas próximos. Você foi severamente criticado."),
                ]
            ),
            Missao(
                "Missão 3: As Águas da Morte",
                "Um rio foi contaminado por uma indústria química. Dr(a). {}, qual será sua estratégia final?".format(self.nome_jogador),
                [
                    Escolha("Biofiltros com bactérias modificadas", {'tecnologico': 2, 'sustentavel': 1}, "A IA controlou bem os biofiltros. O rio voltou a respirar."),
                    Escolha("Consórcios microbianos naturais", {'ecologico': 2, 'sustentavel': 2}, "A natureza começou a se regenerar com sua ajuda inteligente e sensível."),
                    Escolha("Tentar neutralizar com soda cáustica", {'ecologico': -4, 'sustentavel': -2}, "Uma explosão destrói a barragem. O rio está morto. Você será lembrado como o Doutor do Veneno."),
                ]
            )
        ]

    def exibir_missao(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        if self.missao_atual < len(self.missoes):
            missao = self.missoes[self.missao_atual]
            titulo = tk.Label(self.root, text=missao.titulo, font=("Helvetica", 16, "bold"))
            titulo.pack(pady=10)

            narrativa = tk.Label(self.root, text=missao.narrativa, wraplength=600, justify="center")
            narrativa.pack(pady=10)

            for escolha in missao.escolhas:
                botao = tk.Button(self.root, text=escolha.texto, wraplength=500, justify="left",
                                  command=lambda e=escolha: self.processar_escolha(e))
                botao.pack(pady=5)
        else:
            self.finalizar_jogo()

    def processar_escolha(self, escolha):
        for chave in escolha.impacto:
            self.pontuacao[chave] += escolha.impacto[chave]

        messagebox.showinfo("Resultado da Escolha", escolha.resultado)

        if escolha.impacto.get('ecologico', 0) < -4:
            if self.missao_atual == 2:
                messagebox.showerror("Fim", "Suas escolhas levaram à desconfiança global na ciência. Você perdeu sua credibilidade e o mundo perdeu sua chance. Fim de jogo.")
                self.root.quit()
                return
            else:
                messagebox.showwarning("Atenção", "Essa escolha teve consequências graves. Ainda há esperança: você tem mais missões para tentar salvar o planeta.")

        self.missao_atual += 1
        self.exibir_missao()

    def finalizar_jogo(self):
        total = sum(self.pontuacao.values())
        if self.pontuacao['sustentavel'] > 2 and self.pontuacao['ecologico'] > 2:
            final = "FINAL ECORENASER: Graças às suas escolhas sustentáveis e éticas, o planeta começa a se regenerar. Você se torna um símbolo de esperança para a humanidade."
        elif self.pontuacao['tecnologico'] > 3:
            final = "FINAL DOMÍNIO SINTÉTICO: O mundo sobrevive sob controle artificial, mas a natureza foi substituída por tecnologia. Ainda assim, o planeta respira."
        else:
            final = "FINAL INDEFINIDO: Você tentou, mas o equilíbrio foi frágil demais. O mundo cambaleia, esperando novas soluções."

        messagebox.showinfo("Fim do Jogo", final)
        self.root.quit()

if _name_ == "_main_":
    root = tk.Tk()
    jogo = JogoGUI(root)
    root.mainloop()
