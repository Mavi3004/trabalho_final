import tkinter as tk
from tkinter import messagebox

class Missao:
    def _init_(self, titulo, narrativa, escolhas):
        self.titulo = titulo
        self.narrativa = narrativa
        self.escolhas = escolhas

class Escolha:
    def _init_(self, texto, impacto, resultado):
        self.texto = texto
        self.impacto = impacto
        self.resultado = resultado


class InterfacedoJogo:
    def _init_(self, janela):
        self.janela = janela
        self.root.title("🌱 ECOGÊNESE: O LEGADO DO DOUTOR(a)🌍")
        self.janela.geometry("800x600")
        self.nome_jogador = ""
        self.pontuacao = {'ecologico': 0, 'social': 0, 'tecnologico': 0, 'sustentavel': 0}
        self.missoes = self.criar_missoes()
        self.missao_atual = 0
        self.tela_inicial()

    def tela_inicial(self):
        def tela_inicial(self):
        nomedojogo = tk.Label(self.janela, text="🌱 ECOGÊNESE: O LEGADO DO DOUTOR 🌍", font=("Helvetica", 20, "bold"), fg="green")
        nomedojogo.pack(pady=20)

        img = PhotoImage(file="capa3.png")
        capa = tk.Label(self.janela, image=img)
        capa.pack()

        introducao = tk.Label(self.janela, text="Em um planeta à beira do colapso ambiental, onde a poluição devastou florestas, contaminou lençóis freáticos e envenenou o ar das cidades, VOCÊ é a última esperança. Como um brilhante cientista em biotecnologia ambiental, foi recrutado pelo Projeto Ecogênese. Sua missão: usar a ciência e sua sabedoria para salvar ecossistemas devastados. As escolhas são suas. O destino do mundo está em suas mãos. É sua vez de fazer história ou repetir os erros do passado.", wraplength=600, justify="center", font=("Helvetica", 12))
        introducao.pack(pady=30)

        nome_jogador = tk.Label(self.janela, text="Prazer Doutor(a), como você se chama?", font=("Helvetica", 12))
        nome_jogador.pack()

        self.entrada_nome = tk.Entry(self.janela)
        self.entrada_nome.pack(pady=20)

        label_botao = tk.Label(self.janela, text="Preparado(a) para salvar o planeta?", font=("Helvetica", 12))
        label_botao.pack(pady=20)

        botao_iniciar = tk.Button(self.janela, text="Iniciar Jogo", command=self.aoclicar_iniciar)
        botao_iniciar.pack()


    def aoclicar_iniciar(self):
        nome_digitado = self.entrada_nome.get()

        if nome_digitado.strip():
            self.nome_jogador = nome_digitado.strip()
            self.missoes = self.criar_missoes()  # ← agora sim, após o nome ser definido
            self.exibir_missaotela()
        else:
            messagebox.showwarning("Atenção", "Por favor, digite o nome do personagem.")

        
    def criar_missoes(self):
        return [
            Missao(
                "Missão 1: A Cidade Envenenada",
                f"Uma metrópole foi contaminada por metais pesados. Como você, Dr(a). {self.nome_jogador}, irá agir para descontaminar o solo?",
                [
                    Escolha("Usar microrganismos pouco conhecidos para metabolizar os metais", {"ecologico": -2, "tecnologico": 2}, "Os microrganismos funcionaram, mas causaram mutações em insetos locais. A mídia critica sua decisão."),
                    Escolha("Usar plantas hiperacumuladoras de metais", {'ecologico': 2, 'tecnologico': 2}, "As plantas começaram a absorver lentamente os metais. A população aplaude sua paciência e sabedoria."),
                    Escolha("Ignorar protocolos e usar agentes químicos", {'ecologico': -5}, "O solo entrou em combustão! Uma explosão causou caos e poluição aérea.")
                ]
            ),
            Missao(
                "Missão 2: A Floresta Esquecida",
                f"Uma floresta tropical devastada por queimadas precisa ser restaurada. Dr(a). {self.nome_jogador}, qual caminho seguirá?",
                [
                    Escolha("Pulverizar aceleradores genéticos por drones", {'ecologico': -4}, "Uma reação em cadeia de crescimento descontrolado destrói biomas próximos. Você foi severamente criticado."),
                    Escolha("Implantar sementes bioengenheiradas", {'tecnologico': 2, 'sustentavel': -1}, "As árvores crescem rápido, mas algumas espécies dominam e sufocam outras."),
                    Escolha("Reflorestamento com comunidades locais", {'social': 3, 'ecologico': 2}, "As comunidades se unem e a floresta começa a renascer naturalmente.")
                ]
            ),
            Missao(
                "Missão 3: As Águas da Morte",
                f"Um rio foi contaminado por uma indústria química. Dr(a). {self.nome_jogador}, qual será sua estratégia final?",
                [
                    Escolha("Consórcios microbianos naturais", {'ecologico': 2, 'sustentavel': 2}, "A natureza começou a se regenerar com sua ajuda inteligente e sensível."),
                    Escolha("Tentar neutralizar com soda cáustica", {'ecologico': -4, 'sustentavel': -2}, "Uma explosão destrói a barragem. O rio está morto. Você será lembrado como o Doutor do Veneno."),
                    Escolha("Biofiltros com bactérias modificadas", {'tecnologico': 2, 'sustentavel': 1}, "A IA controlou bem os biofiltros. O rio voltou a respirar.")
                ]
            )
        ]


    def exibir_missaotela(self):
                for widget in self.janela.winfo_children():
            widget.destroy()

        if self.missao_atual < len(self.missoes):
            missao = self.missoes[self.missao_atual]

            titulo = tk.Label(self.janela, text=missao.titulo, font=("Helvetica", 16, "bold"))
            titulo.pack(pady=10)

            narrativa = tk.Label(self.janela, text=missao.narrativa, wraplength=600, justify="center")
            narrativa.pack(pady=10)

            for escolha in missao.alternativas:
                botao = tk.Button(self.janela, text=escolha.texto, wraplength=500, justify="left", command=lambda e=escolha: self.calcularImpacto(e))
                botao.pack(pady=10)
        else:
            self.finalizar_jogo()


    def calcularImpacto(self, escolha):
        for chave in escolha.impacto:
            self.pontuacao[chave] += escolha.impacto[chave]

        messagebox.showinfo("Consequência da Escolha", escolha.resultado)

        if escolha.impacto.get('ecologico', 0) < -4:
            if self.missao_atual == 2:
                messagebox.showerror("Fim", "Suas escolhas levaram à desconfiança global na ciência. Você perdeu sua credibilidade e o mundo ficou ainda pior com suas intervenções. Fim de jogo.")
                self.janela.quit()
                return
            else:
                messagebox.showwarning("Atenção", "Essa escolha teve consequências graves. Ainda há esperança: você tem mais missões para tentar salvar o planeta.")
                self.missao_atual += 1
                self.exibir_missaotela()
        else:
            self.missao_atual += 1
            self.exibir_missaotela()


    def finalizar_jogo(self):
        total = sum(self.pontuacao.values())

        if self.pontuacao['sustentavel'] > 2 and self.pontuacao['ecologico'] > 2:
            final = f"FINAL ECORENASCER: Graças às suas escolhas sustentáveis e éticas, Dr(a) {self.nome_jogador}, o planeta começa a se regenerar. Você guiou a humanidade para um futuro verde e justo e se torna um símbolo de esperança para a humanidade."
        elif self.pontuacao['tecnologico'] > 3:
            final = "FINAL DOMÍNIO SINTÉTICO: O mundo sobrevive sob controle artificial, mas a natureza foi substituída por tecnologia. Ainda assim, o planeta respira."
        else:
            final = "VOCÊ FALHOU: Suas tentativas não foram bem sucedidas, o mundo continua em colapso, esperando por novas soluções."

        messagebox.showinfo("Fim do jogo", final)
        self.janela.quit()


# Inicialização da janela principal
janela = tk.Tk()
jogo = InterfacedoJogo(janela)
janela.mainloop()
