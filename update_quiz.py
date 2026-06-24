import sys

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

start_marker = '<!-- Step 1: Para quem é? -->'
end_marker = '<!-- Step 6: Sucesso -->\n                            <div class="quiz-step text-center py-8" id="step-6">\n                                <div class="w-24 h-24 bg-green-100 text-green-600 rounded-full flex items-center justify-center text-5xl mx-auto mb-6 shadow-inner">\n                                    <i class="fa-solid fa-check"></i>\n                                </div>\n                                <h2 class="text-3xl font-bold text-audibel-gray mb-2">Avaliação Liberada!</h2>\n                                <p class="text-gray-600 mb-6">A nossa equipe de especialistas em Curitiba recebeu seus dados e vai te chamar no WhatsApp em instantes para passar todas as informações.</p>\n                            </div>'

start_idx = content.find(start_marker)
end_idx = content.find(end_marker) + len(end_marker)

if start_idx == -1 or end_idx == -1 or end_idx < start_idx:
    print('Markers not found')
    sys.exit(1)

replacement = """<!-- Step 1: Para quem é? -->
                            <div class="quiz-step active" id="step-1">
                                <h3 class="text-xl font-bold text-audibel-gray font-sans uppercase tracking-tight">1. Para quem estamos buscando uma solução auditiva hoje?</h3>
                                <p class="text-sm text-gray-500 mb-4 font-sans italic">Selecione uma das opções abaixo</p>
                                <div class="space-y-3">
                                    <button class="w-full text-left p-4 rounded-xl border-2 border-gray-200 bg-gray-50 hover:border-audibel-red hover:bg-red-50 transition-all font-semibold flex items-center gap-4 quiz-option group" data-target="step-2" data-answer="Para mim" data-progress="30%">
                                        <div class="w-10 h-10 rounded-full bg-white flex items-center justify-center text-audibel-gray group-hover:bg-audibel-red group-hover:text-white transition-colors shadow-sm"><i class="fa-solid fa-user"></i></div>
                                        Para mim mesmo(a)
                                    </button>
                                    <button class="w-full text-left p-4 rounded-xl border-2 border-gray-200 bg-gray-50 hover:border-audibel-red hover:bg-red-50 transition-all font-semibold flex items-center gap-4 quiz-option group" data-target="step-2" data-answer="Para um familiar" data-progress="30%">
                                        <div class="w-10 h-10 rounded-full bg-white flex items-center justify-center text-audibel-gray group-hover:bg-audibel-red group-hover:text-white transition-colors shadow-sm"><i class="fa-solid fa-users"></i></div>
                                        Para um familiar (pai, mãe, cônjuge)
                                    </button>
                                </div>
                            </div>

                            <!-- Step 2: Faixa Etária -->
                            <div class="quiz-step" id="step-2">
                                <button class="text-sm text-gray-400 hover:text-audibel-red mb-4 back-btn font-bold uppercase tracking-wider" data-target="step-1" data-progress="15%"><i class="fa-solid fa-arrow-left"></i> Voltar</button>
                                <h3 class="text-xl font-bold text-audibel-gray font-sans uppercase tracking-tight">2. Qual é a faixa etária da pessoa?</h3>
                                <p class="text-sm text-gray-500 mb-4 font-sans italic">Selecione uma das opções abaixo</p>
                                <div class="space-y-3">
                                    <button class="w-full text-left p-4 rounded-xl border-2 border-gray-200 bg-gray-50 hover:border-audibel-red hover:bg-red-50 transition-all font-semibold flex items-center gap-4 quiz-option group" data-target="step-3" data-answer="Abaixo de 50" data-progress="45%">
                                        <div class="w-10 h-10 rounded-full bg-white flex items-center justify-center text-audibel-gray group-hover:bg-audibel-red group-hover:text-white transition-colors shadow-sm"><i class="fa-solid fa-person"></i></div>
                                        Abaixo de 50 anos
                                    </button>
                                    <button class="w-full text-left p-4 rounded-xl border-2 border-gray-200 bg-gray-50 hover:border-audibel-red hover:bg-red-50 transition-all font-semibold flex items-center gap-4 quiz-option group" data-target="step-3" data-answer="50 a 65" data-progress="45%">
                                        <div class="w-10 h-10 rounded-full bg-white flex items-center justify-center text-audibel-gray group-hover:bg-audibel-red group-hover:text-white transition-colors shadow-sm"><i class="fa-solid fa-person-walking"></i></div>
                                        Entre 50 e 65 anos
                                    </button>
                                    <button class="w-full text-left p-4 rounded-xl border-2 border-gray-200 bg-gray-50 hover:border-audibel-red hover:bg-red-50 transition-all font-semibold flex items-center gap-4 quiz-option group" data-target="step-3" data-answer="Acima de 65" data-progress="45%">
                                        <div class="w-10 h-10 rounded-full bg-white flex items-center justify-center text-audibel-gray group-hover:bg-audibel-red group-hover:text-white transition-colors shadow-sm"><i class="fa-solid fa-person-cane"></i></div>
                                        Acima de 65 anos
                                    </button>
                                </div>
                            </div>

                            <!-- Step 3: Histórico (Efeito Gaveta) -->
                            <div class="quiz-step" id="step-3">
                                <button class="text-sm text-gray-400 hover:text-audibel-red mb-4 back-btn font-bold uppercase tracking-wider" data-target="step-2" data-progress="30%"><i class="fa-solid fa-arrow-left"></i> Voltar</button>
                                <h3 class="text-xl font-bold text-audibel-gray font-sans uppercase tracking-tight">3. Qual é a experiência atual com aparelhos auditivos?</h3>
                                <p class="text-sm text-gray-500 mb-4 font-sans italic">Selecione uma das opções abaixo</p>
                                <div class="space-y-3">
                                    <button class="w-full text-left p-4 rounded-xl border-2 border-gray-200 bg-gray-50 hover:border-audibel-red hover:bg-red-50 transition-all font-semibold flex items-center gap-4 quiz-option group" data-target="step-4" data-answer="Nunca usou" data-progress="60%">
                                        <div class="w-10 h-10 rounded-full bg-white flex items-center justify-center text-audibel-gray group-hover:bg-audibel-red group-hover:text-white transition-colors shadow-sm"><i class="fa-solid fa-ear-deaf"></i></div>
                                        Nunca usou aparelhos auditivos
                                    </button>
                                    <button class="w-full text-left p-4 rounded-xl border-2 border-gray-200 bg-gray-50 hover:border-audibel-red hover:bg-red-50 transition-all font-semibold flex items-center gap-4 quiz-option group" data-target="step-4" data-answer="Já usa" data-progress="60%">
                                        <div class="w-10 h-10 rounded-full bg-white flex items-center justify-center text-audibel-gray group-hover:bg-audibel-red group-hover:text-white transition-colors shadow-sm"><i class="fa-solid fa-ear-listen"></i></div>
                                        Já usa, mas busca uma opção melhor
                                    </button>
                                </div>
                            </div>

                            <!-- Step 4: Situação de Necessidade (Diagnóstico) - Múltipla Escolha -->
                            <div class="quiz-step" id="step-4">
                                <button class="text-sm text-gray-400 hover:text-audibel-red mb-4 back-btn font-bold uppercase tracking-wider" data-target="step-3" data-progress="45%"><i class="fa-solid fa-arrow-left"></i> Voltar</button>
                                <h3 class="text-xl font-bold text-audibel-gray font-sans uppercase tracking-tight">4. Para quais destas situações você mais precisa do aparelho?</h3>
                                <p class="text-sm text-gray-500 mb-4 font-sans italic">Selecione uma ou mais opções abaixo</p>
                                <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 mb-4">
                                    <button class="text-left p-4 rounded-xl border-2 border-gray-200 bg-gray-50 hover:border-audibel-red hover:bg-red-50 transition-all font-semibold text-sm quiz-multi-option" data-answer="Assistir TV, ouvir música ou falar ao celular">
                                        <div class="flex items-center justify-between">
                                            <span>Assistir TV, ouvir música ou falar ao celular</span>
                                            <i class="fa-solid fa-check text-audibel-red opacity-0 check-icon"></i>
                                        </div>
                                    </button>
                                    <button class="text-left p-4 rounded-xl border-2 border-gray-200 bg-gray-50 hover:border-audibel-red hover:bg-red-50 transition-all font-semibold text-sm quiz-multi-option" data-answer="Conversas em grupo ou ambientes barulhentos">
                                         <div class="flex items-center justify-between">
                                            <span>Acompanhar conversas em grupo ou ambientes barulhentos</span>
                                            <i class="fa-solid fa-check text-audibel-red opacity-0 check-icon"></i>
                                        </div>
                                    </button>
                                    <button class="text-left p-4 rounded-xl border-2 border-gray-200 bg-gray-50 hover:border-audibel-red hover:bg-red-50 transition-all font-semibold text-sm quiz-multi-option" data-answer="Zumbido">
                                         <div class="flex items-center justify-between">
                                            <span>Aliviar incômodo do zumbido</span>
                                            <i class="fa-solid fa-check text-audibel-red opacity-0 check-icon"></i>
                                        </div>
                                    </button>
                                    <button class="text-left p-4 rounded-xl border-2 border-gray-200 bg-gray-50 hover:border-audibel-red hover:bg-red-50 transition-all font-semibold text-sm quiz-multi-option" data-answer="Sons do dia a dia">
                                         <div class="flex items-center justify-between">
                                            <span>Ouvir sons do dia a dia (telefone, campainha, alarmes)</span>
                                            <i class="fa-solid fa-check text-audibel-red opacity-0 check-icon"></i>
                                        </div>
                                    </button>
                                </div>
                                <button id="btn-continue-step-4" class="w-full bg-audibel-red text-white p-4 rounded-xl font-bold uppercase transition-all duration-300 opacity-50 cursor-not-allowed hover:bg-audibel-red hover:shadow-lg disabled:hover:bg-audibel-red disabled:hover:shadow-none" disabled>Continuar</button>
                            </div>

                            <!-- Step 5: Nível de Desconforto -->
                            <div class="quiz-step" id="step-5">
                                <button class="text-sm text-gray-400 hover:text-audibel-red mb-4 back-btn font-bold uppercase tracking-wider" data-target="step-4" data-progress="60%"><i class="fa-solid fa-arrow-left"></i> Voltar</button>
                                <h3 class="text-xl font-bold text-audibel-gray font-sans uppercase tracking-tight">5. Qual é o nível desse desconforto hoje?</h3>
                                <p class="text-sm text-gray-500 mb-4 font-sans italic">Selecione uma das opções abaixo</p>
                                <div class="space-y-3">
                                    <button class="w-full text-left p-4 rounded-xl border-2 border-gray-200 bg-gray-50 hover:border-audibel-red hover:bg-red-50 transition-all font-semibold quiz-option flex items-center" data-target="step-6" data-answer="Leve" data-progress="100%">
                                        <span class="inline-block w-3 h-3 rounded-full bg-yellow-400 mr-3 shadow-sm"></span> Leve (Incomoda às vezes)
                                    </button>
                                    <button class="w-full text-left p-4 rounded-xl border-2 border-gray-200 bg-gray-50 hover:border-audibel-red hover:bg-red-50 transition-all font-semibold quiz-option flex items-center" data-target="step-6" data-answer="Moderado" data-progress="100%">
                                        <span class="inline-block w-3 h-3 rounded-full bg-orange-500 mr-3 shadow-sm"></span> Moderado (Atrapalha conversas)
                                    </button>
                                    <button class="w-full text-left p-4 rounded-xl border-2 border-gray-200 bg-gray-50 hover:border-audibel-red hover:bg-red-50 transition-all font-semibold quiz-option flex items-center" data-target="step-6" data-answer="Alto" data-progress="100%">
                                        <span class="inline-block w-3 h-3 rounded-full bg-red-600 mr-3 shadow-sm"></span> Alto (Gera isolamento social)
                                    </button>
                                </div>
                            </div>

                            <!-- Step 6: Captura de Lead -->
                            <div class="quiz-step" id="step-6">
                                <button class="text-sm text-gray-400 hover:text-audibel-red mb-4 back-btn font-bold uppercase tracking-wider" data-target="step-5" data-progress="80%"><i class="fa-solid fa-arrow-left"></i> Voltar</button>
                                <h2 class="text-3xl font-bold text-audibel-red mb-2">Quase lá!</h2>
                                <p class="text-sm text-gray-600 mb-6 font-sans">
                                    Para não corrermos o risco de passar um valor de um aparelho que não resolva essa dificuldade, liberamos seu **Check-up Auditivo Gratuito**. Preencha para enviarmos o orçamento completo:
                                </p>
                                
                                <form id="lead-form" class="space-y-4">
                                    <div>
                                        <label class="block text-sm font-semibold mb-1 text-audibel-gray">Seu Nome</label>
                                        <input type="text" id="lead-name" required class="w-full p-3 border border-gray-300 bg-gray-50 rounded-lg focus:outline-none focus:border-audibel-red focus:ring-1 focus:ring-audibel-red" placeholder="Digite seu nome completo">
                                    </div>
                                    <div>
                                        <label class="block text-sm font-semibold mb-1 text-audibel-gray">Seu WhatsApp</label>
                                        <input type="tel" id="lead-phone" required class="w-full p-3 border border-gray-300 bg-gray-50 rounded-lg focus:outline-none focus:border-audibel-red focus:ring-1 focus:ring-audibel-red" placeholder="(41) 99999-9999">
                                    </div>
                                    <button type="submit" class="w-full btn-primary font-barlow text-xl py-4 rounded-brand uppercase font-bold flex justify-center items-center gap-2 mt-4 shadow-lg">
                                        <i class="fa-solid fa-unlock-keyhole"></i> Liberar minha Avaliação
                                    </button>
                                </form>
                            </div>

                            <!-- Step 7: Sucesso -->
                            <div class="quiz-step text-center py-8" id="step-7">
                                <div class="w-24 h-24 bg-green-100 text-green-600 rounded-full flex items-center justify-center text-5xl mx-auto mb-6 shadow-inner">
                                    <i class="fa-solid fa-check"></i>
                                </div>
                                <h2 class="text-3xl font-bold text-audibel-gray mb-2">Avaliação Liberada!</h2>
                                <p class="text-gray-600 mb-6">A nossa equipe de especialistas em Curitiba recebeu seus dados e vai te chamar no WhatsApp em instantes para passar todas as informações.</p>
                            </div>"""

new_content = content[:start_idx] + replacement + content[end_idx:]

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(new_content)
print('HTML replacement done.')
