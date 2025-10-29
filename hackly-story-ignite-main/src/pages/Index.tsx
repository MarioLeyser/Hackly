import Navigation from "@/components/Navigation";
import Hero from "@/components/Hero";
import AboutSection from "@/components/AboutSection";
import StorytellingSection from "@/components/StorytellingSection";
import TrySection from "@/components/TrySection";
import CommunitySection from "@/components/CommunitySection";
import Footer from "@/components/Footer";

const Index = () => {
  return (
    <div className="min-h-screen">
      <Navigation />
      <Hero />
      <AboutSection />
      <StorytellingSection />
      <TrySection />
      <CommunitySection />
      <Footer />
    </div>
  );
};

export default Index;
