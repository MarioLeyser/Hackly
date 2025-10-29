import { Card, CardContent } from "@/components/ui/card";
import { Badge } from "@/components/ui/badge";
import { Button } from "@/components/ui/button";
import { MessageSquare, Heart, Users, ExternalLink } from "lucide-react";

const CommunitySection = () => {
  const partners = [
    {
      name: "Incubadora DE1551",
      description: "Universidad Nacional Mayor de San Marcos",
      icon: "🎓",
    },
    {
      name: "Infortelgraf Perú",
      description: "Tecnología para el desarrollo",
      icon: "💻",
    },
    {
      name: "Tinkuy Wasi",
      description: "Conectando comunidades",
      icon: "🤝",
    },
    {
      name: "IEEE Student Branch",
      description: "Innovación tecnológica estudiantil",
      icon: "⚡",
    },
  ];

  const stats = [
    { value: "300+", label: "Estudiantes Activos", icon: <Users className="w-6 h-6" /> },
    { value: "50+", label: "Proyectos Realizados", icon: <Heart className="w-6 h-6" /> },
    { value: "10+", label: "Comunidades Impactadas", icon: <MessageSquare className="w-6 h-6" /> },
  ];

  return (
    <section id="comunidad" className="py-20 bg-gradient-to-b from-muted/20 to-background">
      <div className="container mx-auto px-4">
        <div className="max-w-6xl mx-auto space-y-12">
          {/* Header */}
          <div className="text-center space-y-4">
            <Badge variant="outline" className="mb-2">
              <Users className="w-3 h-3 mr-1" />
              Comunidad
            </Badge>
            <h2 className="text-4xl md:text-5xl font-bold">
              Somos una{" "}
              <span className="bg-gradient-to-r from-primary to-secondary bg-clip-text text-transparent">
                red de cambio
              </span>
            </h2>
            <p className="text-xl text-muted-foreground max-w-2xl mx-auto">
              Trabajamos junto a organizaciones comprometidas con el desarrollo educativo y comunitario
            </p>
          </div>

          {/* Stats */}
          <div className="grid md:grid-cols-3 gap-6">
            {stats.map((stat, index) => (
              <Card
                key={index}
                className="text-center border-2 hover:border-primary transition-all hover:shadow-lg"
              >
                <CardContent className="pt-6 space-y-3">
                  <div className="text-primary mx-auto w-fit">{stat.icon}</div>
                  <div className="text-4xl font-bold bg-gradient-to-r from-primary to-secondary bg-clip-text text-transparent">
                    {stat.value}
                  </div>
                  <div className="text-sm text-muted-foreground">{stat.label}</div>
                </CardContent>
              </Card>
            ))}
          </div>

          {/* Partners */}
          <div className="space-y-6">
            <h3 className="text-2xl font-bold text-center">Nuestros Aliados</h3>
            <div className="grid md:grid-cols-2 lg:grid-cols-4 gap-6">
              {partners.map((partner, index) => (
                <Card
                  key={index}
                  className="text-center hover:shadow-lg transition-all hover:-translate-y-1"
                >
                  <CardContent className="pt-6 space-y-3">
                    <div className="text-5xl mb-2">{partner.icon}</div>
                    <h4 className="font-bold">{partner.name}</h4>
                    <p className="text-sm text-muted-foreground">{partner.description}</p>
                  </CardContent>
                </Card>
              ))}
            </div>
          </div>

          {/* CTA */}
          <div className="text-center space-y-6 bg-gradient-to-br from-primary/5 via-secondary/5 to-accent/5 p-12 rounded-2xl border-2">
            <h3 className="text-3xl font-bold">¿Quieres ser parte?</h3>
            <p className="text-muted-foreground max-w-2xl mx-auto">
              Si tu organización está comprometida con el desarrollo educativo y comunitario,
              nos encantaría colaborar contigo
            </p>
            <Button
              size="lg"
              variant="outline"
              className="border-2"
            >
              Contactar
              <ExternalLink className="ml-2 w-4 h-4" />
            </Button>
          </div>
        </div>
      </div>
    </section>
  );
};

export default CommunitySection;
