import re
import os
import spacy
from tqdm import tqdm 
import pandas as pd 
BASEDIR= os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class Lemma:
	# def __init__(self):
	# 	pass

	def lemma_spacy(liste):
		"""
		Lemmatisierung mit Spacy

		: param :		liste: list
		: return:		dict: ein dict mit den keys: 'lemma', 'text', 'position'
		"""
		word_lemma = []
		word_text = []
		word_pos = []
		word_dict = {}
		nlp = spacy.load("de")
		#doc = nlp(df['freude'])
		for item in tqdm(liste):
		    doc = nlp(str(item))
		    for token in doc:
		        word_lemma.append(token.lemma_)
		        word_text.append(token.text)
		        word_pos.append(token.pos_)
		word_dict['lemma'] = word_lemma
		word_dict['text'] = word_text
		word_dict['position'] = word_pos
		return word_dict


class Emotionen_rklinger:

	def __init__(self):
		self.ekel_lexicon = []
		self.freude_lexicon = []
		self.furcht_lexicon = []
		self.trauer_lexicon = []
		self.ueberraschung_lexicon = []
		self.verachtung_lexicon = []
		self.wut_lexicon = []

	def show(self):
		print("	1.	Ekel")
		print("	2.	Freude")
		print("	3.	Furcht")
		print("	4.	Trauer")
		print("	5.	Überraschung")
		print("	6.	Verachtung")
		print("	7.	Wut")

	def load_ekel(self):
		self.ekel_file = open(os.path.join(BASEDIR+'/txtanalysis'+'/fundamental'+'/ekel.txt'), 'r')
		for item in self.ekel_file:
			low= item.lower() 
			rep= low.replace("\n","")
			self.ekel_lexicon.append(rep)
		return self.ekel_lexicon

	def load_freude(self):
		self.freude_file = open(os.path.join(BASEDIR+'/txtanalysis'+'/fundamental'+'/freude.txt'), 'r')
		for item in self.freude_file:
			low= item.lower() 
			rep= low.replace("\n","")
			self.freude_lexicon.append(rep)
		return self.freude_lexicon

	def load_furcht(self):
		self.furcht_file = open(os.path.join(BASEDIR+'/txtanalysis'+'/fundamental'+'/furcht.txt'), 'r')
		for item in self.furcht_file:
			low= item.lower() 
			rep= low.replace("\n","")
			self.furcht_lexicon.append(rep)
		return self.furcht_lexicon

	def load_trauer(self):
		self.trauer_file = open(os.path.join(BASEDIR+'/txtanalysis'+'/fundamental'+'/trauer.txt'), 'r')
		for item in self.trauer_file:
			low= item.lower() 
			rep= low.replace("\n","")
			self.trauer_lexicon.append(rep)
		return self.trauer_lexicon

	def load_ueberraschung(self):
		self.ueberraschung_file = open(os.path.join(BASEDIR+'/txtanalysis'+'/fundamental'+'/ueberraschung.txt'), 'r')
		for item in self.ueberraschung_file:
			low= item.lower() 
			rep= low.replace("\n","")
			self.ueberraschung_lexicon.append(rep)
		return self.ueberraschung_lexicon

	def load_verachtung(self):
		self.verachtung_file = open(os.path.join(BASEDIR+'/txtanalysis'+'/fundamental'+'/verachtung.txt'), 'r')
		for item in self.verachtung_file:
			low= item.lower() 
			rep= low.replace("\n","")
			self.verachtung_lexicon.append(rep)
		return self.verachtung_lexicon

	def load_wut(self):
		self.wut_file = open(os.path.join(BASEDIR+'/txtanalysis'+'/fundamental'+'/wut.txt'), 'r')
		for item in self.wut_file:
			low= item.lower() 
			rep= low.replace("\n","")
			self.wut_lexicon.append(rep)
		return self.wut_lexicon

	def extract_words(self,data, lexicon):
		sentiment_words = []
		for item in data: 
			for element in lexicon:
				if item == element:
					sentiment_words.append(item)
				else:
					continue
		return sentiment_words

class Emotionen_nrc: 

    def NRC_analysis(token_c):
        """
        *** EMOTION ANALYSIS WITH NRC_de.csv ***
        1. Zorn
        2. Erwartung
        3. Ekel
        4. Furcht
        5. Freude
        6. Traurigkeit
        7. Überraschung
        8. Vertrauen

        : param : token_c : list with lower()
        : return : emotionslisten : zorn_liste, erwartung_liste, ekel_liste, furcht_liste, freude_liste, traurigkeit_liste, überraschung_liste, vertrauen_liste

        """
        nrc1 = pd.read_csv(os.path.join(BASEDIR +'/txtanalysis' +'/NRC_de.csv'),delimiter=';')  
        nrc = nrc1.apply(lambda x: x.astype(str))
        Zorn = 0
        Erwartung = 0
        Ekel = 0
        Furcht = 0 
        Freude = 0 
        Traurigkeit = 0 
        Überraschung = 0 
        Vertrauen = 0
        zorn_liste = []
        erwartung_liste = []
        ekel_liste = []
        furcht_liste = []
        freude_liste = []
        traurigkeit_liste = []
        überraschung_liste = []
        vertrauen_liste = []
        cc = 0 
        for i in token_c:
            if nrc['Wort'].isin([i]).any():
                cc += 1
                # ZORN
                if ((nrc['Wort'] == i) & (nrc['Zorn'] == '1')).any():
                    Zorn += 1
                    print(f"{cc} Zorn <--- ", i)
                    zorn_liste.append(i)
                # ERWARTUNG
                if ((nrc['Wort'] == i) & (nrc['Erwartung'] == '1')).any():
                    Erwartung += 1
                    print(f"{cc} Erwartung <--- ",i)
                    erwartung_liste.append(i)
                # EKEL
                if ((nrc['Wort'] == i) & (nrc['Ekel'] == '1')).any():
                    Ekel += 1
                    print(f"{cc} Ekel <--- ",i)
                    ekel_liste.append(i)
                # FURCHT
                if ((nrc['Wort'] == i) & (nrc['Furcht'] == '1')).any():
                    Furcht += 1
                    print(f"{cc} Furcht <--- ",i)
                    furcht_liste.append(i)
                # FREUDE
                if ((nrc['Wort'] == i) & (nrc['Freude'] == '1')).any():
                    Freude += 1
                    print(f"{cc} Freude <--- ",i)
                    freude_liste.append(i)
                # TRAURIGKEIT
                if ((nrc['Wort'] == i) & (nrc['Traurigkeit'] == '1')).any():
                    Traurigkeit += 1
                    print(f"{cc} Traurigkeit <--- ",i)
                    traurigkeit_liste.append(i)
                # ÜBERRASCHUNG
                if ((nrc['Wort'] == i) & (nrc['Überraschung'] == '1')).any():
                    Überraschung += 1
                    print(f"{cc} Überraschung <--- ",i)
                    überraschung_liste.append(i)
                # VERTRAUEN
                if ((nrc['Wort'] == i) & (nrc['Vertrauen'] == '1')).any():
                    Vertrauen += 1
                    print(f"{cc} Vertrauen <--- ",i)
                    vertrauen_liste.append(i)
        print("Zorn 		<---		:", Zorn)
        print("Erwartung 	<---		:",Erwartung)
        print("Ekel 		<---		:",Ekel)
        print("Furcht 		<---		:",Furcht)
        print("Freude 		<---		:",Freude)
        print("Traurigkeit 	<---		:",Traurigkeit)
        print("Überraschung <---		:",Überraschung)
        print("Vertrauen 	<---		:",Vertrauen)
        print("_________________")
        print("Words totally found: ",cc, " *")
        print("_________________")
        xf = Zorn + Erwartung + Ekel + Furcht + Freude + Traurigkeit + Überraschung + Vertrauen
        EI = xf/ len(token_c) # token_c remove stop_words len()
        try:
            faktor = xf/cc
        except:
            faktor= 0 
        print("EMOTIONEN  = ", xf, " *")
        print("FAKTOR = ", xf/cc)
        return EI, faktor, zorn_liste, erwartung_liste, ekel_liste, furcht_liste, freude_liste, traurigkeit_liste, überraschung_liste, vertrauen_liste








