import { Card, CardContent } from "@/components/ui/card";
import { Badge } from "@/components/ui/badge";
import { Users, Target, Lightbulb } from "lucide-react";
import lauraPhoto from "@/assets/team-laura.jpg";

const AboutSection = () => {
  const team = [
    { name: "Laura Valentina Rodríguez Ore", role: "CEO", photo: lauraPhoto },
    { name: "Martín Jair Huamani Condeña", role: "CTO", photo: null },
    { name: "Mario Leyser Vilca Zamora", role: "CISO", photo: null },
    { name: "William Anthony Chambi Huacantara", role: "CFO", photo: null },
  ];

  return (
    <section id="nosotros" className="py-20 bg-gradient-to-b from-background to-muted/20">
      <div className="container mx-auto px-4">
        <div className="max-w-6xl mx-auto space-y-16">
          {/* Header */}
          <div className="text-center space-y-4">
            <Badge variant="outline" className="mb-2">
              <Users className="w-3 h-3 mr-1" />
              Sobre Nosotros
            </Badge>
            <h2 className="text-4xl md:text-5xl font-bold">
              Conoce a{" "}
              <span className="bg-gradient-to-r from-primary to-secondary bg-clip-text text-transparent">
                Hackly
              </span>
            </h2>
          </div>

          {/* Mission Statement */}
          <div className="grid md:grid-cols-3 gap-6">
            <Card className="border-2 hover:border-primary transition-all hover:shadow-lg">
              <CardContent className="pt-6">
                <Target className="w-10 h-10 text-primary mb-4" />
                <h3 className="text-xl font-bold mb-2">Nuestra Misión</h3>
                <p className="text-muted-foreground">
                  Transformar la manera en que los jóvenes interactúan con los problemas de su comunidad.
                </p>
              </CardContent>
            </Card>
            <Card className="border-2 hover:border-secondary transition-all hover:shadow-lg">
              <CardContent className="pt-6">
                <Lightbulb className="w-10 h-10 text-secondary mb-4" />
                <h3 className="text-xl font-bold mb-2">Nuestra Visión</h3>
                <p className="text-muted-foreground">
                  Cada historia puede convertirse en acción a través de la gamificación y el aprendizaje práctico.
                </p>
              </CardContent>
            </Card>
            <Card className="border-2 hover:border-accent transition-all hover:shadow-lg">
              <CardContent className="pt-6">
                <Users className="w-10 h-10 text-accent mb-4" />
                <h3 className="text-xl font-bold mb-2">Nuestro Impacto</h3>
                <p className="text-muted-foreground">
                  Cualquier persona puede convertirse en un agente de cambio en su comunidad.
                </p>
              </CardContent>
            </Card>
          </div>

          {/* Description */}
          <div className="bg-card rounded-2xl p-8 border shadow-soft space-y-6">
            <p className="text-lg leading-relaxed">
              <strong className="text-primary">Hackly</strong> es un equipo multidisciplinario apasionado por transformar 
              la manera en que los jóvenes interactúan con los problemas de su comunidad. Nuestra plataforma combina{" "}
              <span className="font-semibold text-secondary">storytelling</span> e{" "}
              <span className="font-semibold text-accent">inteligencia artificial</span> para guiar a los usuarios 
              en la creación de proyectos con impacto real, cambiando narrativas y generando soluciones innovadoras.
            </p>

            <p className="text-lg leading-relaxed">
              Contamos con experiencia en llegar a zonas vulnerables, gracias a nuestra conexión con la{" "}
              <span className="font-semibold">Incubadora 1551</span> de la Universidad Nacional Mayor de San Marcos
              y con diversas ONG y organizaciones aliadas como <span className="font-semibold">Infortelgraf Perú</span>,{" "}
              <span className="font-semibold">Tinkuy Wasi</span> y{" "}
              <span className="font-semibold">IEEE Student Branch</span>, quienes apoyan la difusión de nuestra 
              propuesta entre estudiantes y universitarios de primeros ciclos.
            </p>

            <div className="pt-4">
              <Badge className="bg-gradient-to-r from-primary to-secondary text-white">
                Innovación educativa y desarrollo comunitario
              </Badge>
            </div>
          </div>

          {/* Team */}
          <div className="space-y-8">
            <div className="text-center">
              <h3 className="text-3xl font-bold mb-2">Nuestro Equipo</h3>
              <p className="text-muted-foreground">
                Creemos que cada historia puede convertirse en acción
              </p>
            </div>

            <div className="grid md:grid-cols-2 lg:grid-cols-4 gap-6">
              {team.map((member, index) => (
                <Card
                  key={index}
                  className="text-center hover:shadow-lg transition-all hover:-translate-y-1"
                >
                  <CardContent className="pt-6 space-y-4">
                    {/* Photo */}
                    <div className="w-32 h-32 mx-auto rounded-full overflow-hidden border-4 border-background shadow-medium bg-gradient-to-br from-primary/20 to-secondary/20 flex items-center justify-center">
                      {member.photo ? (
                        <img 
                          src={member.photo} 
                          alt={member.name}
                          className="w-full h-full object-cover"
                        />
                      ) : (
                        <Users className="w-16 h-16 text-primary/60" />
                      )}
                    </div>
                    <div>
                      <h4 className="font-bold text-lg mb-1">{member.name}</h4>
                      <Badge variant="secondary">{member.role}</Badge>
                    </div>
                  </CardContent>
                </Card>
              ))}
            </div>
          </div>
        </div>
      </div>
    </section>
  );
};

export default AboutSection;
