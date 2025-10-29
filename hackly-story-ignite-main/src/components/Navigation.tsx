import { useState } from "react";
import { Menu, X } from "lucide-react";
import { Button } from "@/components/ui/button";
import hacklyLogo from "@/assets/hackly-logo.png";

const Navigation = () => {
  const [isOpen, setIsOpen] = useState(false);
  const [language, setLanguage] = useState("es");

  const navItems = {
    es: [
      { name: "Nosotros", href: "#nosotros" },
      { name: "Storytelling", href: "#storytelling" },
      { name: "Pruébate", href: "#pruebate" },
      { name: "Comunidad", href: "#comunidad" },
    ],
    en: [
      { name: "About Us", href: "#nosotros" },
      { name: "Storytelling", href: "#storytelling" },
      { name: "Try It", href: "#pruebate" },
      { name: "Community", href: "#comunidad" },
    ],
    qu: [
      { name: "Ñuqanchikta", href: "#nosotros" },
      { name: "Willakuy", href: "#storytelling" },
      { name: "Pruébaykuy", href: "#pruebate" },
      { name: "Ayllu", href: "#comunidad" },
    ],
  };

  const languages = [
    { code: "es", name: "Español" },
    { code: "en", name: "English" },
    { code: "qu", name: "Quechua" },
  ];

  const scrollToSection = (href: string) => {
    const element = document.querySelector(href);
    element?.scrollIntoView({ behavior: "smooth" });
    setIsOpen(false);
  };

  return (
    <nav className="fixed top-0 left-0 right-0 z-50 bg-background/80 backdrop-blur-lg border-b border-border">
      <div className="container mx-auto px-4 py-4">
        <div className="flex items-center justify-between">
          <div className="flex items-center gap-3">
            <img src={hacklyLogo} alt="Hackly Logo" className="h-12 w-12" />
            <div>
              <h1 className="text-xl font-bold bg-gradient-to-r from-primary to-secondary bg-clip-text text-transparent">
                HACKLY
              </h1>
              <p className="text-xs text-muted-foreground">
                {language === "es" && "Gestión de proyectos para estudiantes"}
                {language === "en" && "Project management for students"}
                {language === "qu" && "Yachaqkunapaq ruwanakuna kamachiy"}
              </p>
            </div>
          </div>

          {/* Desktop Navigation */}
          <div className="hidden md:flex items-center gap-6">
            {navItems[language as keyof typeof navItems].map((item) => (
              <button
                key={item.name}
                onClick={() => scrollToSection(item.href)}
                className="text-sm font-medium text-foreground hover:text-primary transition-colors"
              >
                {item.name}
              </button>
            ))}
            <select
              value={language}
              onChange={(e) => setLanguage(e.target.value)}
              className="text-sm font-medium bg-transparent border border-border rounded-lg px-3 py-2 cursor-pointer hover:border-primary transition-colors"
            >
              {languages.map((lang) => (
                <option key={lang.code} value={lang.code}>
                  {lang.name}
                </option>
              ))}
            </select>
          </div>

          {/* Mobile Menu Button */}
          <Button
            variant="ghost"
            size="icon"
            className="md:hidden"
            onClick={() => setIsOpen(!isOpen)}
          >
            {isOpen ? <X /> : <Menu />}
          </Button>
        </div>

        {/* Mobile Menu */}
        {isOpen && (
          <div className="md:hidden mt-4 pb-4 space-y-4">
            {navItems[language as keyof typeof navItems].map((item) => (
              <button
                key={item.name}
                onClick={() => scrollToSection(item.href)}
                className="block w-full text-left text-sm font-medium text-foreground hover:text-primary transition-colors py-2"
              >
                {item.name}
              </button>
            ))}
            <select
              value={language}
              onChange={(e) => setLanguage(e.target.value)}
              className="w-full text-sm font-medium bg-transparent border border-border rounded-lg px-3 py-2 cursor-pointer"
            >
              {languages.map((lang) => (
                <option key={lang.code} value={lang.code}>
                  {lang.name}
                </option>
              ))}
            </select>
          </div>
        )}
      </div>
    </nav>
  );
};

export default Navigation;
