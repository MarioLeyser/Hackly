import { Card, CardContent } from "@/components/ui/card";
import { Badge } from "@/components/ui/badge";
import { Zap, Trophy, Users, Target } from "lucide-react";
import QuizTest from "./QuizTest";

const TrySection = () => {
  const features = [
    {
      icon: <Zap className="w-10 h-10" />,
      title: "Aprende Haciendo",
      description: "Resuelve retos reales de tu comunidad con metodología gamificada",
      color: "text-primary",
    },
    {
      icon: <Trophy className="w-10 h-10" />,
      title: "Gana Reconocimiento",
      description: "Obtén badges y certificados por tus proyectos de impacto social",
      color: "text-secondary",
    },
    {
      icon: <Users className="w-10 h-10" />,
      title: "Conecta con tu Comunidad",
      description: "Trabaja en equipo y crea redes de colaboración local",
      color: "text-accent",
    },
    {
      icon: <Target className="w-10 h-10" />,
      title: "Crea Impacto Real",
      description: "Transforma tus ideas en soluciones que mejoran vidas",
      color: "text-success",
    },
  ];

  return (
    <section id="pruebate" className="py-20 bg-gradient-to-b from-background to-muted/20">
      <div className="container mx-auto px-4">
        <div className="max-w-6xl mx-auto space-y-12">
          {/* Header */}
          <div className="text-center space-y-4">
            <Badge variant="outline" className="mb-2">
              <Zap className="w-3 h-3 mr-1" />
              Pruébate
            </Badge>
            <h2 className="text-4xl md:text-5xl font-bold">
              ¿Listo para{" "}
              <span className="bg-gradient-to-r from-primary to-accent bg-clip-text text-transparent">
                marcar la diferencia?
              </span>
            </h2>
            <p className="text-xl text-muted-foreground max-w-2xl mx-auto">
              Hackly te proporciona todas las herramientas que necesitas para convertir
              tus ideas en proyectos de impacto real
            </p>
          </div>

          {/* Features Grid */}
          <div className="grid md:grid-cols-2 gap-6">
            {features.map((feature, index) => (
              <Card
                key={index}
                className="border-2 hover:border-primary/50 transition-all hover:shadow-lg hover:-translate-y-1"
              >
                <CardContent className="pt-6 space-y-4">
                  <div className={`${feature.color}`}>{feature.icon}</div>
                  <h3 className="text-2xl font-bold">{feature.title}</h3>
                  <p className="text-muted-foreground">{feature.description}</p>
                </CardContent>
              </Card>
            ))}
          </div>

          {/* Quiz Test CTA */}
          <div className="bg-gradient-to-r from-primary/10 via-secondary/10 to-accent/10 p-12 rounded-2xl border-2 border-primary/20">
            <QuizTest />
          </div>
        </div>
      </div>
    </section>
  );
};

export default TrySection;
