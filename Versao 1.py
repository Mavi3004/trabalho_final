import tkinter as tk
from tkinter import messagebox

class Missao:  # Classe que define a interface das missões
    def __init__(self, titulo, narrativa, escolhas):
        self.titulo = titulo
        self.narrativa = narrativa
        self.alternativas = escolhas

class Escolha:  # Classe que define as alternativas
    def __init__(self, texto, impacto, resultado):
        self.texto = texto
        self.impacto = impacto
        self.resultado = resultado

class InterfacedoJogo:
    def __init__(self, janela):
        self.janela = janela
        self.janela.title("🌱 ECOGÊNESE: O LEGADO DO DOUTOR(a) 🌍")
        self.janela.geometry("1000x800")
        self.nome_jogador = ""
        self.pontuacao = {'risco': 0, 'tecnologico': 0, 'sustentavel': 0, 'ecologico': 0}
        self.missoes = self.criar_missoes()
        self.missao_atual = 0

        self.tela_inicial()

    def tela_inicial(self):
        nomedojogo = tk.Label(self.janela, text="🌱 ECOGÊNESE: O LEGADO DO DOUTOR 🌍", font=("Helvetica", 20, "bold"), fg="green")
        nomedojogo.pack(pady=10)

        self.imagem = tk.PhotoImage(file="capa3.png")
        label = tk.Label(self.janela, image=self.imagem)
        label.pack()

        introducao = tk.Label(self.janela, text="Em um planeta à beira do colapso ambiental, onde a poluição devastou florestas, contaminou lençóis freáticos e envenenou o ar das cidades, VOCÊ é a última esperança. Como um brilhante cientista em biotecnologia ambiental, foi recrutado pelo Projeto Ecogênese. Sua missão: usar a ciência e sua sabedoria para salvar ecossistemas devastados. As escolhas são suas. O destino do mundo está em suas mãos. É sua vez de fazer história ou repetir os erros do passado.", wraplength=600, justify="center", font=("Helvetica", 12))
        introducao.pack(pady=10)

        nome_jogador = tk.Label(self.janela, text="Prazer Doutor(a), como você se chama?", font=("Helvetica", 12))
        nome_jogador.pack()

        self.entrada_nome = tk.Entry(self.janela)
        self.entrada_nome.pack()

        label_botao = tk.Label(self.janela, text="Preparado(a) para salvar o planeta?", font=("Helvetica", 12))
        label_botao.pack()

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

    def reiniciar_jogo(self):
        self.nome_jogador = ""
        self.pontuacao = {'risco': 0, 'tecnologico': 0, 'sustentavel': 0, 'ecologico': 0}
        self.missao_atual = 0
        
        for widget in self.janela.winfo_children():
            widget.destroy()
            
        self.tela_inicial()


    def criar_missoes(self):
        return [
            Missao(
                "Missão 1: A Cidade Envenenada",
                f"Uma metrópole industrial está enfrentando uma grave crise ambiental após décadas de descarte inadequado de resíduos. Altos níveis de metais pesados foram detectados no solo, afetando plantações urbanas, lençóis freáticos e a saúde da população local. As autoridades estão pressionadas por respostas rápidas, mas a complexidade do problema exige decisões estratégicas. Como você, Dr(a). {self.nome_jogador}, especialista em biotecnologia ambiental, irá abordar a descontaminação desse solo crítico?",
                [
                    Escolha("Aplicar consórcios microbianos pouco testados, geneticamente adaptados para metabolizar metais pesados.", {"risco":-1,"tecnologico": 2, "sustentavel":0,"ecologico": 2}, "Os microrganismos demonstraram alta eficiência na quebra de compostos tóxicos, mas sua interação com o ecossistema urbano gerou mutações inesperadas em insetos locais. Especialistas alertam para possíveis desequilíbrios biológicos, e parte da população teme uma nova forma de contaminação invisível."),
                    Escolha("Iniciar um programa de fitorremediação utilizando espécies vegetais hiperacumuladoras para absorção lenta dos metais.", {"risco":0,"tecnologico": 1, "sustentavel":3,"ecologico": 2}, "As plantas começaram a extrair metais do solo com segurança, embora o processo seja lento e demande cuidados constantes. Enquanto isso, algumas áreas continuam impróprias para uso. A população reconhece o esforço sustentável, mas cobra mais urgência das autoridades."),
                    Escolha("Utilizar agentes químicos de neutralização rápida, ignorando parte dos protocolos ambientais.", {"risco":-2,"tecnologico": 0, "sustentavel":0,"ecologico": 1}, "A reação química foi veloz, mas gerou subprodutos instáveis que atingiram o lençol freático. Um incêndio subterrâneo se alastrou, exigindo evacuação de bairros inteiros. A mídia expõe falhas no controle da operação, e sua reputação científica é colocada em dúvida.")
                ]
            ),
            Missao(
                "Missão 2: A Floresta Esquecida",
                f"Uma antiga floresta tropical, devastada por queimadas consecutivas e desmatamento ilegal, encontra-se em processo de desertificação. Parte da biodiversidade foi perdida, e o solo está empobrecido. Como você, Dr(a). {self.nome_jogador}, pretende conduzir a restauração ecológica desse bioma em risco?",
                [
                    Escolha("Pulverizar aceleradores genéticos por drones para estimular o crescimento vegetal imediato", {"risco":-2,"tecnologico": 2, "sustentavel":0,"ecologico": 0}, "O uso dos aceleradores causou um crescimento descontrolado de espécies vegetais, resultando em um bioma artificial denso, mas instável. Espécies invasoras se proliferaram, sufocando a diversidade original. Ambientalistas e comunidades locais criticam a abordagem por ignorar os processos naturais de regeneração."),
                    Escolha("Implantar sementes bioengenheiradas adaptadas ao solo degradado", {"risco":-1,"tecnologico": 3, "sustentavel":0,"ecologico": 1}, "As sementes modificadas germinaram rapidamente, mas favoreceram poucas espécies dominantes. O equilíbrio ecológico não foi totalmente restaurado, e cientistas alertam para possíveis impactos a longo prazo na cadeia alimentar. Ainda assim, a paisagem começa a se recuperar visualmente."),
                    Escolha("Promover reflorestamento participativo com as comunidades locais e espécies nativas", {"risco":0,"tecnologico": 0, "sustentavel":1,"ecologico": 3}, "A regeneração natural, combinada com o envolvimento das populações locais, trouxe resultados lentos, mas consistentes. A diversidade original começa a ressurgir e os vínculos sociais se fortalecem. Embora mais demorado, o processo é visto como exemplo de sustentabilidade integrada")
                ]
            ),
            Missao(
                "Missão 3: As Águas da Morte",
                f"Um rio vital para comunidades ribeirinhas foi contaminado por efluentes industriais contendo resíduos orgânicos e metais pesados. O ecossistema aquático colapsou, e surtos de doenças começaram a surgir. A empresa responsável nega culpa e pressiona por soluções rápidas. Você, Dr(a). {self.nome_jogador}, precisa decidir como intervir nesse sistema altamente comprometido.",
                [
                    Escolha("Aplicar consórcios microbianos naturais para estimular a biorremediação do rio", {"risco":0,"tecnologico": 3, "sustentavel":2,"ecologico": 2}, "A diversidade microbiana nativa foi reativada e, com o tempo, a qualidade da água começou a melhorar. Apesar da lentidão inicial, o processo foi bem aceito pelas comunidades e gerou um modelo replicável de recuperação ambiental baseada em soluções naturais."),
                    Escolha("Tentar neutralizar os poluentes com soda cáustica", {"risco":-2,"tecnologico": 0, "sustentavel":0,"ecologico": 0}, "A neutralização química causou reações violentas com os compostos presentes no rio, liberando calor e gases tóxicos. Uma ruptura na contenção provocou alagamentos e contaminação secundária. A empresa tentou minimizar os danos, mas o desastre ganhou repercussão internacional. Você será lembrado como o Doutor do Veneno."),
                    Escolha("Instalar biofiltros com bactérias geneticamente modificadas para remoção seletiva de contaminantes", {"risco":-1,"tecnologico": 3, "sustentavel":1,"ecologico": 0}, "Os biofiltros mostraram alta eficácia na retenção de metais e compostos orgânicos. O controle automatizado ajudou na estabilidade do sistema, mas levantou debates sobre a liberação de organismos modificados no ambiente. A recuperação foi significativa, mas sob monitoramento constante.")
                ]
            )
        ]

    def exibir_missaotela(self):
        for widget in self.janela.winfo_children():
            widget.destroy()

        if self.missao_atual < len(self.missoes):
            missao = self.missoes[self.missao_atual]

            titulo = tk.Label(self.janela, text=missao.titulo, font=("Helvetica", 20, "bold"),fg="green")
            titulo.pack(pady=10)

            narrativa = tk.Label(self.janela, text=missao.narrativa, wraplength=600,font=("Helvetica", 16), justify="center")
            narrativa.pack(pady=10)

            for escolha in missao.alternativas:
                botao = tk.Button(self.janela, text=escolha.texto, wraplength=500, justify="left",font=("Helvetica", 14), command=lambda e=escolha: self.calcularImpacto(e))
                botao.pack(pady=10)
        else:
            self.finalizar_jogo()

    def calcularImpacto(self, escolha):
        for chave in escolha.impacto:
            self.pontuacao[chave] += escolha.impacto[chave]

        messagebox.showinfo("Consequência da Escolha", escolha.resultado)

        if escolha.impacto.get('risco', 0) == -2:
            if self.missao_atual == 0:
                
                messagebox.showwarning("Atenção", "Essa escolha teve consequências graves. Ainda há esperança: você tem mais missões para tentar salvar o planeta.")
                
        
        self.missao_atual += 1
        self.exibir_missaotela()

    def finalizar_jogo(self):
        for widget in self.janela.winfo_children():
            widget.destroy()
        
        total = sum(self.pontuacao.values())

        if self.pontuacao['risco'] <= 0 and self.pontuacao['tecnologico'] <= 7 and self.pontuacao['sustentavel'] >= 3 and self.pontuacao['ecologico'] >= 4:
            final = f"🌿FINAL ECORENASCER: Graças às suas decisões baseadas em soluções sustentáveis, inclusivas e baseadas na natureza, Dr(a). {self.nome_jogador}, ecossistemas começaram a se regenerar, populações se reaproximaram do meio ambiente e políticas públicas foram influenciadas por suas ações. Sua trajetória tornou-se referência global em biotecnologia ambiental aliada à justiça ecológica. O planeta, embora ainda vulnerável, respira com esperança renovada."

        elif self.pontuacao['risco'] <= -2 and self.pontuacao['tecnologico'] >= 5 and self.pontuacao['sustentavel'] <= 4 and self.pontuacao['ecologico'] <= 5:
            final = "🧬FINAL BIOINTEGRAÇÃO: Suas escolhas priorizaram o uso de biotecnologias avançadas como principal resposta às crises ambientais. Bactérias programadas, sementes bioengenheiradas e sistemas automatizados regeneraram ambientes antes considerados perdidos. Embora algumas regiões naturais tenham sido substituídas por sistemas controlados, você criou um novo paradigma: a coexistência entre engenharia biológica e natureza. O mundo que emerge é híbrido — meio natural, meio projetado — mas viável e resiliente."
        else:
            final = "☠️FINAL COLAPSO ECOSSISTÊMICO: Suas decisões, embora bem-intencionadas, foram marcadas por riscos mal calculados, negligência com a complexidade ambiental ou pressa por resultados imediatos. Contaminações se intensificaram, populações foram deslocadas e a confiança na ciência ambiental foi profundamente abalada. O planeta entrou em uma nova era de escassez e conflito. Seu nome será lembrado, mas como um alerta para os limites entre intervenção e destruição."


        label_final = tk.Label(self.janela, text=final, wraplength=700, justify="center", font=("Helvetica", 14))
        label_final.pack(pady=30)

        botao_reiniciar = tk.Button(self.janela, text="🔄 Jogar Novamente", font=("Helvetica", 12), command=self.reiniciar_jogo)
        botao_reiniciar.pack(pady=10)

        botao_sair = tk.Button(self.janela, text="❌ Sair", font=("Helvetica", 12), command=self.janela.destroy)
        botao_sair.pack(pady=5)


# Inicialização da janela principal
janela = tk.Tk()
jogo = InterfacedoJogo(janela)
janela.mainloop()
