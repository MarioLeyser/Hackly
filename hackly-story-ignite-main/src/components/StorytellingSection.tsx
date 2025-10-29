import { useState } from "react";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { Button } from "@/components/ui/button";
import { Textarea } from "@/components/ui/textarea";
import { Badge } from "@/components/ui/badge";
import { Sparkles, RefreshCw, Send, Info } from "lucide-react";
import { toast } from "sonner";

interface Challenge {
  titulo: string;
  historia: string;
  imagen: string;
  datos: string[];
  feedbacks: string[];
}

const StorytellingSection = () => {
  const [currentChallenge, setCurrentChallenge] = useState<Challenge | null>(null);
  const [dataIndex, setDataIndex] = useState(0);
  const [response, setResponse] = useState("");
  const [feedback, setFeedback] = useState("");

  const challenges: Challenge[] = [
    {
      titulo: "Violencia doméstica en zonas rurales",
      historia: "Mariela vive en una comunidad andina donde muchas mujeres no denuncian por miedo o falta de acceso a ayuda. No hay señal, ni comisaría cercana. Ella necesita una solución silenciosa y segura.",
      imagen: "https://www.rel-uita.org/wp-content/uploads/2022/11/20211207_Appeq-1400.jpg",
      datos: [
        "Solo 3 de cada 10 mujeres rurales denuncian la violencia que sufren.",
        "Muchas veces no cuentan con celulares propios ni redes de apoyo local.",
        "Las radios comunitarias son uno de los pocos medios de comunicación disponibles.",
      ],
      feedbacks: [
        "¿Podrías pensar en una solución que funcione offline o con señales de emergencia no digitales?",
        "¿Cómo incluirías a actores locales como promotores de salud o líderes comunales?",
        "Considera el uso de alertas visuales o codificadas. ¿Tu propuesta podría ser anónima?",
      ],
    },
    {
      titulo: "Abandono escolar post-pandemia",
      historia: "Luis, de 14 años, dejó de ir a la escuela para ayudar a su madre vendiendo en el mercado. La pandemia desmotivó a muchos niños a volver al aula. ¿Cómo podrías motivarlo a continuar?",
      imagen: "https://cloudfront-eu-central-1.images.arcpublishing.com/prisa/MPI63FTKJUUZGXYWH4WLRW5BMA.jpg",
      datos: [
        "En algunas zonas rurales de Perú, más del 35% de estudiantes no retornaron después de la pandemia.",
        "La mayoría trabaja para apoyar económicamente a sus familias.",
        "La falta de conectividad limita el acceso a educación virtual.",
      ],
      feedbacks: [
        "¿Cómo harías atractiva la educación nuevamente para jóvenes como Luis?",
        "¿Tu propuesta funciona sin internet o recursos tecnológicos avanzados?",
        "Considera alinear el aprendizaje con actividades productivas. ¿Es posible?",
      ],
    },
    {
      titulo: "Acceso al agua limpia en barrios vulnerables",
      historia: "En Villa Esperanza, los vecinos solo reciben agua dos horas al día. Niños como Leyser beben agua almacenada con bacterias. ¿Cómo podrías mejorar esta situación?",
      imagen: "https://blogs.worldbank.org/content/dam/sites/blogs/img/detail/mgr/agua_0_0-701.jpg",
      datos: [
        "El 25% de viviendas en Lima no tiene acceso continuo a agua potable.",
        "El agua almacenada por más de 24h en baldes sin tapa genera riesgo de enfermedades.",
        "Las fugas invisibles en tuberías domiciliarias son una causa común de pérdida.",
      ],
      feedbacks: [
        "¿Has considerado sensores de bajo costo para detectar fugas?",
        "Tu propuesta podría incorporar filtros caseros o sistemas comunitarios.",
        "¿Cómo educarías a las familias sobre almacenamiento seguro del agua?",
      ],
    },
    {
      titulo: "Educación Digital en Iztapalapa",
      historia: "Juan, de 14 años, vive en Iztapalapa, Ciudad de México. Quiere aprender a programar, pero su escuela tiene solo 5 computadoras para 300 alumnos. Usa una cabina de internet cuando puede. ¿Cómo facilitarle el acceso sin depender del internet ni equipos caros?",
      imagen: "https://cdn-3.expansion.mx/dims4/default/e7deae5/2147483647/strip/true/crop/6000x4000+0+0/resize/1200x800!/format/webp/quality/60/?url=https%3A%2F%2Fcherry-brightspot.s3.amazonaws.com%2Fbc%2Ff6%2F0aa03d824f169fcadda985e95c08%2Fcapacitate-0225.jpg",
      datos: [
        "Apps como Kolibri y servidores Raspberry Pi se han usado en zonas sin conectividad.",
        "ONGs han creado kioscos educativos móviles con contenido precargado.",
      ],
      feedbacks: [
        "¿Podrías usar hardware local o apps offline para escalar tu idea?",
        "¿Tu solución puede replicarse fácilmente en otras escuelas de bajos recursos?",
      ],
    },
  ];

  const showChallenge = () => {
    const randomIndex = Math.floor(Math.random() * challenges.length);
    setCurrentChallenge(challenges[randomIndex]);
    setDataIndex(0);
    setResponse("");
    setFeedback("");
  };

  const handleSendResponse = () => {
    if (!response.trim()) {
      toast.error("Por favor, escribe una propuesta");
      return;
    }

    if (currentChallenge) {
      const feedbackIndex = Math.min(dataIndex, currentChallenge.feedbacks.length - 1);
      setFeedback(currentChallenge.feedbacks[feedbackIndex]);
      toast.success("Feedback generado");
    }
  };

  const handleContinue = () => {
    if (!currentChallenge) return;

    if (dataIndex < currentChallenge.datos.length) {
      setDataIndex(dataIndex + 1);
      setFeedback("");
      setResponse("");
      toast.info("Nuevo dato desbloqueado");
    } else {
      toast.success("Has explorado toda la información de este reto");
    }
  };

  return (
    <section id="storytelling" className="py-20 bg-gradient-to-b from-muted/20 to-background">
      <div className="container mx-auto px-4">
        <div className="max-w-4xl mx-auto space-y-8">
          {/* Header */}
          <div className="text-center space-y-4">
            <Badge variant="outline" className="mb-2">
              <Sparkles className="w-3 h-3 mr-1" />
              Simulador Interactivo
            </Badge>
            <h2 className="text-4xl md:text-5xl font-bold">
              <span className="bg-gradient-to-r from-primary to-secondary bg-clip-text text-transparent">
                Storytelling
              </span>{" "}
              Hackathon
            </h2>
            <p className="text-xl text-muted-foreground">
              Aprende a resolver problemas reales de tu comunidad
            </p>
          </div>

          {/* Challenge Card */}
          <Card className="shadow-medium border-2">
            <CardHeader>
              <CardTitle className="flex items-center gap-2">
                🎯 Simulador de Hackathon
              </CardTitle>
            </CardHeader>
            <CardContent className="space-y-6">
              {!currentChallenge ? (
                <div className="text-center py-12">
                  <p className="text-muted-foreground mb-6">
                    Inicia tu viaje de innovación social
                  </p>
                  <Button
                    onClick={showChallenge}
                    size="lg"
                    className="bg-gradient-to-r from-primary to-secondary hover:opacity-90"
                  >
                    <Sparkles className="mr-2 w-4 h-4" />
                    Comenzar reto
                  </Button>
                </div>
              ) : (
                <>
                  {/* Challenge Image */}
                  <img
                    src={currentChallenge.imagen}
                    alt={currentChallenge.titulo}
                    className="w-full h-64 object-cover rounded-lg"
                  />

                  {/* Challenge Description */}
                  <div className="space-y-2">
                    <h3 className="text-xl font-bold text-primary">
                      {currentChallenge.titulo}
                    </h3>
                    <p className="text-foreground leading-relaxed">
                      {currentChallenge.historia}
                    </p>
                  </div>

                  {/* Extra Data */}
                  {dataIndex > 0 && dataIndex <= currentChallenge.datos.length && (
                    <div className="bg-success/10 border-l-4 border-success p-4 rounded-lg">
                      <div className="flex gap-2">
                        <Info className="w-5 h-5 text-success flex-shrink-0 mt-0.5" />
                        <div>
                          <p className="font-semibold text-success mb-1">
                            Dato adicional:
                          </p>
                          <p className="text-sm">
                            {currentChallenge.datos[dataIndex - 1]}
                          </p>
                        </div>
                      </div>
                    </div>
                  )}

                  {/* Response Input */}
                  <Textarea
                    value={response}
                    onChange={(e) => setResponse(e.target.value)}
                    placeholder="Escribe tu propuesta aquí..."
                    className="min-h-[120px]"
                  />

                  {/* Feedback */}
                  {feedback && (
                    <div className="bg-primary/10 border-l-4 border-primary p-4 rounded-lg">
                      <p className="font-semibold text-primary mb-1">📝 Feedback:</p>
                      <p className="text-sm">{feedback}</p>
                    </div>
                  )}

                  {/* Actions */}
                  <div className="flex flex-wrap gap-3">
                    <Button onClick={handleSendResponse} className="flex-1 min-w-[200px]">
                      <Send className="mr-2 w-4 h-4" />
                      Enviar respuesta
                    </Button>
                    <Button
                      onClick={handleContinue}
                      variant="outline"
                      className="flex-1 min-w-[200px]"
                    >
                      Continuar con el reto
                    </Button>
                    <Button
                      onClick={showChallenge}
                      variant="secondary"
                      className="flex-1 min-w-[200px]"
                    >
                      <RefreshCw className="mr-2 w-4 h-4" />
                      Cambiar de reto
                    </Button>
                  </div>
                </>
              )}
            </CardContent>
          </Card>
        </div>
      </div>
    </section>
  );
};

export default StorytellingSection;
