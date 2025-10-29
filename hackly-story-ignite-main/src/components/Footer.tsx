import hacklyLogo from "@/assets/hackly-logo.png";

const Footer = () => {
  return (
    <footer className="bg-muted/30 border-t">
      <div className="container mx-auto px-4 py-12">
        <div className="max-w-6xl mx-auto grid md:grid-cols-3 gap-8">
          {/* Brand */}
          <div className="space-y-4">
            <div className="flex items-center gap-3">
              <img src={hacklyLogo} alt="Hackly Logo" className="h-10 w-10" />
              <div>
                <h3 className="font-bold text-lg">HACKLY</h3>
                <p className="text-xs text-muted-foreground">
                  Project management for students
                </p>
              </div>
            </div>
            <p className="text-sm text-muted-foreground">
              Transformando historias de tu comunidad en proyectos de impacto real
            </p>
          </div>

          {/* Links */}
          <div>
            <h4 className="font-semibold mb-4">Enlaces</h4>
            <ul className="space-y-2 text-sm text-muted-foreground">
              <li>
                <a href="#nosotros" className="hover:text-primary transition-colors">
                  Sobre Nosotros
                </a>
              </li>
              <li>
                <a href="#storytelling" className="hover:text-primary transition-colors">
                  Storytelling
                </a>
              </li>
              <li>
                <a href="#pruebate" className="hover:text-primary transition-colors">
                  Pruébate
                </a>
              </li>
              <li>
                <a href="#comunidad" className="hover:text-primary transition-colors">
                  Comunidad
                </a>
              </li>
            </ul>
          </div>

          {/* Contact */}
          <div>
            <h4 className="font-semibold mb-4">Contacto</h4>
            <ul className="space-y-2 text-sm text-muted-foreground">
              <li>📧 contacto@hackly.com</li>
              <li>📍 Lima, Perú</li>
              <li>🏫 UNMSM - Incubadora 1551</li>
            </ul>
          </div>
        </div>

        <div className="mt-8 pt-8 border-t text-center text-sm text-muted-foreground">
          <p>© 2024 Hackly. Innovación educativa y desarrollo comunitario.</p>
        </div>
      </div>
    </footer>
  );
};

export default Footer;
