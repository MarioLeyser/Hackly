import { useState } from "react";
import { Button } from "@/components/ui/button";
import { Card, CardContent } from "@/components/ui/card";

interface Question {
  q: string;
  options: string[];
  answer: number;
}

interface Questions {
  basico: Question[];
  intermedio: Question[];
  avanzado: Question[];
}

const questions: Questions = {
  basico: [
    { q: '¿Cuál es la definición más simple de un proyecto?', options: ['Un proceso continuo', 'Una actividad repetitiva', 'Un esfuerzo temporal con un objetivo específico', 'Un departamento dentro de la empresa'], answer: 2 },
    { q: '¿Qué documento describe formalmente el alcance y objetivos al inicio?', options: ['Plan de comunicación', 'Acta de constitución (Project Charter)', 'Registro de riesgos', 'Cronograma'], answer: 1 },
    { q: '¿Qué representa el triángulo de gestión de proyectos?', options: ['Tiempo, costo y alcance', 'Calidad, riesgo y alcance', 'Recursos, clima y clientes', 'Alcance, financiación y personas'], answer: 0 }
  ],
  intermedio: [
    { q: '¿Qué es una matriz RACI?', options: ['Un cronograma avanzado', 'Una matriz de responsabilidades', 'Un presupuesto detallado', 'Una técnica de estimación'], answer: 1 },
    { q: '¿Cuál es la diferencia entre riesgo y problema?', options: ['No hay diferencia', 'Riesgo es futuro; problema ya ocurrió', 'Riesgo siempre es negativo', 'Problema siempre es financiero'], answer: 1 },
    { q: '¿Qué técnica ayuda a priorizar tareas según valor y esfuerzo?', options: ['Diagrama de Gantt', 'Matriz valor/esfuerzo', 'EVM', 'Análisis FODA'], answer: 1 }
  ],
  avanzado: [
    { q: '¿Qué mide el Valor Ganado (EVM)?', options: ['Calidad del producto', 'Desempeño en alcance, tiempo y coste', 'Satisfacción del cliente', 'Rendimiento del equipo'], answer: 1 },
    { q: '¿Cuál es la fórmula del CPI (Cost Performance Index)?', options: ['CPI = EV / AC', 'CPI = AC / EV', 'CPI = PV / EV', 'CPI = EV - AC'], answer: 0 },
    { q: '¿Qué técnica cuantitativa evalúa la incertidumbre mediante simulación?', options: ['Análisis FODA', 'Técnica Delphi', 'Simulación Monte Carlo', 'Diagrama de Pareto'], answer: 2 }
  ]
};

type Level = 'basico' | 'intermedio' | 'avanzado';

const QuizTest = () => {
  const [currentLevel, setCurrentLevel] = useState<Level | null>(null);
  const [currentIndex, setCurrentIndex] = useState(0);
  const [userAnswers, setUserAnswers] = useState<(number | undefined)[]>([]);
  const [showResults, setShowResults] = useState(false);
  const [selectedOption, setSelectedOption] = useState<number | undefined>(undefined);

  const startQuiz = (level: Level) => {
    setCurrentLevel(level);
    setCurrentIndex(0);
    setUserAnswers([]);
    setShowResults(false);
    setSelectedOption(undefined);
  };

  const handleOptionSelect = (optionIndex: number) => {
    setSelectedOption(optionIndex);
    const newAnswers = [...userAnswers];
    newAnswers[currentIndex] = optionIndex;
    setUserAnswers(newAnswers);
  };

  const handleNext = () => {
    if (!currentLevel) return;
    
    if (selectedOption === undefined) {
      alert('Selecciona una opción antes de continuar.');
      return;
    }

    const total = questions[currentLevel].length;
    if (currentIndex < total - 1) {
      setCurrentIndex(currentIndex + 1);
      setSelectedOption(userAnswers[currentIndex + 1]);
    } else {
      setShowResults(true);
    }
  };

  const handlePrev = () => {
    if (currentIndex > 0) {
      setCurrentIndex(currentIndex - 1);
      setSelectedOption(userAnswers[currentIndex - 1]);
    }
  };

  const calculateResults = () => {
    if (!currentLevel) return { correctCount: 0, total: 0 };
    const bank = questions[currentLevel];
    let correctCount = 0;
    bank.forEach((q, i) => {
      if (userAnswers[i] === q.answer) correctCount++;
    });
    return { correctCount, total: bank.length };
  };

  const capitalize = (s: string) => s.charAt(0).toUpperCase() + s.slice(1);

  if (!currentLevel) {
    return (
      <div className="space-y-6">
        <div className="text-center space-y-4">
          <h3 className="text-3xl font-bold">Evalúa tu nivel de conocimiento</h3>
          <p className="text-muted-foreground max-w-2xl mx-auto">
            Pruébate en conocimiento de gestión de proyectos y refuerza tus conocimientos
          </p>
        </div>
        <div className="flex flex-col md:flex-row gap-4 justify-center">
          <Button
            size="lg"
            onClick={() => startQuiz('basico')}
            variant="outline"
            className="hover:bg-primary/10"
          >
            Básico
          </Button>
          <Button
            size="lg"
            onClick={() => startQuiz('intermedio')}
            variant="outline"
            className="hover:bg-secondary/10"
          >
            Intermedio
          </Button>
          <Button
            size="lg"
            onClick={() => startQuiz('avanzado')}
            variant="outline"
            className="hover:bg-accent/10"
          >
            Avanzado
          </Button>
        </div>
      </div>
    );
  }

  if (showResults) {
    const { correctCount, total } = calculateResults();
    const bank = questions[currentLevel];

    return (
      <div className="space-y-6">
        <Card>
          <CardContent className="pt-6 space-y-4">
            <h3 className="text-2xl font-bold">Resultado Final</h3>
            <p className="text-xl">
              <strong>{correctCount}</strong> / {total} respuestas correctas
            </p>
            
            <div className="space-y-4 mt-6">
              <h4 className="font-bold">Desglose de respuestas:</h4>
              {bank.map((q, i) => {
                const chosen = userAnswers[i];
                const isCorrect = chosen === q.answer;
                return (
                  <div key={i} className="border-t pt-4">
                    <div className="font-semibold">Pregunta {i + 1}: {q.q}</div>
                    <div className={isCorrect ? "text-success" : "text-danger"}>
                      Tu respuesta: {chosen !== undefined ? q.options[chosen] : 'Sin seleccionar'} {isCorrect ? '✅' : '❌'}
                    </div>
                    {!isCorrect && (
                      <div className="text-muted-foreground">
                        Respuesta correcta: {q.options[q.answer]}
                      </div>
                    )}
                  </div>
                );
              })}
            </div>

            <Button onClick={() => setCurrentLevel(null)} className="mt-6">
              Volver a elegir nivel
            </Button>
          </CardContent>
        </Card>
      </div>
    );
  }

  const qObj = questions[currentLevel][currentIndex];
  const total = questions[currentLevel].length;

  return (
    <Card>
      <CardContent className="pt-6 space-y-6">
        <div className="flex justify-between items-center">
          <h3 className="text-xl font-bold">Nivel: {capitalize(currentLevel)}</h3>
          <span className="text-muted-foreground">
            Pregunta {currentIndex + 1} / {total}
          </span>
        </div>

        <div className="space-y-4">
          <div className="font-semibold text-lg">{qObj.q}</div>
          <div className="space-y-3">
            {qObj.options.map((opt, i) => (
              <button
                key={i}
                onClick={() => handleOptionSelect(i)}
                className={`w-full p-4 text-left rounded-lg border-2 transition-all ${
                  selectedOption === i
                    ? 'border-primary bg-primary/10'
                    : 'border-border hover:border-primary/50'
                }`}
              >
                {opt}
              </button>
            ))}
          </div>
        </div>

        <div className="flex justify-between gap-4">
          <Button
            onClick={handlePrev}
            disabled={currentIndex === 0}
            variant="outline"
          >
            Anterior
          </Button>
          <Button onClick={handleNext} className="bg-primary">
            {currentIndex === total - 1 ? 'Finalizar' : 'Siguiente'}
          </Button>
        </div>
      </CardContent>
    </Card>
  );
};

export default QuizTest;
