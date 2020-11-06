import re
import os
import spacy
from tqdm import tqdm 
import pandas as pd 
from txtanalysis.utils import DataWrangling as DW

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


class NRC_analysis:

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


class Utils:
    def select_df(keyword, df):
        """
        GET NEW DATA FRAME BASED ON KEYWORD
        
        : keyword: keyword: str z.B: "Coronavirus"
        : df : loaded dataframe
        : return : result: Dataframe
        
        """
        
        #keyy = str(input("Welches Keyword? "))
        keyy = keyword
        cc = 0
        cj = 0
        index_keyword = []
        for i in df['keywords']:
            x2 = i.replace("[","") 
            x1 = x2.replace("]","")
            x = x1.replace("'","")
            ss = x.strip().split(",")
            for j in ss:
                jj = j.strip()
                if jj == keyy:
                    index_keyword.append(cc)
                    cj += 1

            cc += 1
        print(f"Anzahl an Artikel mit {keyword}" , len(index_corona))
        
        ndf = pd.DataFrame()
        ndfl = []
        for j in index_keyword:
            f = df.iloc[j]
            #print(f)
            ndfl.append(f)
        result = pd.DataFrame(ndfl).reset_index()
        return result

class NRC_analysis: 

    def NRC_analysis(token_c, show=False, show_results=False , not_found=False):
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

        : param : token_c : token splitted list (token_c = [i.split() for i in data])
        : return : EmotionIndex(EI), cc(Gefundene Wörter im NRC), CountOhneSTP(Wörter ohne Stopwörter), Faktor(Emotion/Words)
		: return : emotionslisten : zorn_liste, erwartung_liste, ekel_liste, furcht_liste, freude_liste, traurigkeit_liste, überraschung_liste, vertrauen_liste
        """
        print("--------------------------------------------------")
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
        nF = []
        for i in token_c:
            if nrc['Wort'].isin([i]).any():
                cc += 1
                # ZORN
                if ((nrc['Wort'] == i) & (nrc['Zorn'] == '1')).any():
                    Zorn += 1
                    zorn_liste.append(i)
                    if show_results == True:
                        print(f"{cc} Zorn <--- ", i)
                # ERWARTUNG
                if ((nrc['Wort'] == i) & (nrc['Erwartung'] == '1')).any():
                    Erwartung += 1
                    erwartung_liste.append(i)
                    if show_results == True:
                        print(f"{cc} Erwartung <--- ",i)
                # EKEL
                if ((nrc['Wort'] == i) & (nrc['Ekel'] == '1')).any():
                    Ekel += 1
                    ekel_liste.append(i)
                    if show_results == True:
                        print(f"{cc} Ekel <--- ",i)
                # FURCHT
                if ((nrc['Wort'] == i) & (nrc['Furcht'] == '1')).any():
                    Furcht += 1
                    furcht_liste.append(i)
                    if show_results == True:
                        print(f"{cc} Furcht <--- ",i)
                # FREUDE
                if ((nrc['Wort'] == i) & (nrc['Freude'] == '1')).any():
                    Freude += 1
                    freude_liste.append(i)
                    if show_results == True:
                        print(f"{cc} Freude <--- ",i)
                # TRAURIGKEIT
                if ((nrc['Wort'] == i) & (nrc['Traurigkeit'] == '1')).any():
                    Traurigkeit += 1
                    traurigkeit_liste.append(i)
                    if show_results == True:
                        print(f"{cc} Traurigkeit <--- ",i)
                # ÜBERRASCHUNG
                if ((nrc['Wort'] == i) & (nrc['Überraschung'] == '1')).any():
                    Überraschung += 1
                    überraschung_liste.append(i)
                    if show_results == True:
                        print(f"{cc} Überraschung <--- ",i)
                # VERTRAUEN
                if ((nrc['Wort'] == i) & (nrc['Vertrauen'] == '1')).any():
                    Vertrauen += 1
                    vertrauen_liste.append(i)
                    if show_results == True:
                        print(f"{cc} Vertrauen <--- ",i)
            else:
                nF.append(i)
                if not_found == True:
                    print(f"++ Not found: ++ {i}")
        if show == True:
            print("--------------------------------------------------")
            print("Freude       <---        :",Freude)
            print("Vertrauen    <---        :",Vertrauen)
            print("Angst       <---        :",Furcht)
            print("Überraschung    <---     :",Überraschung)
            print("Traurigkeit  <---        :",Traurigkeit)
            print("Ekel         <---        :",Ekel)
            print("Ärger 		<---		:", Zorn)
            print("Erwartung 	<---		:",Erwartung)
            
        xf = Zorn + Erwartung + Ekel + Furcht + Freude + Traurigkeit + Überraschung + Vertrauen # Anzahl der gefundenen Emotionen 
        stopwrd = DW.load_stopwords() 
        no_stp = DW.remove_stopwords(token_c, stopwrd)
        EI = xf/ len(no_stp) # EmotionsIndex
        CountOhneSTP=  len(no_stp)
        try:
            faktor = xf/cc
        except:
            faktor= 0
        stp_wörter = len(token_c) - CountOhneSTP
        prozent_stp = stp_wörter * 100 / len(token_c)
        if show == True:
            print("___________________________________________________") 
            print("TOTAL WORDS = ", len(token_c))
            print("WORDS FOUND = ", cc)
            print("EMOTIONEN FOUND = ", xf, " *")
            print("FAKTOR = ", faktor)
            print("EmotionIndex = ", EI)
            print("WORDS OHNE STOP = ", len(no_stp))
            print("Prozent an STOP = ", round(prozent_stp,2), "%")
            print("")
            print("Hinweis:")
            print("EmotionIndex = Emotionen/Words ohne Stopwords")
            print("Words = gefundene Wörter im NRC")
            print("Emotionen = Gesamtanzahl an Emotionen")
            print("Faktor = Emotionen/ Words")
            print("")
            print("___________________________________________________")

        emo_dict = {'Freude': freude_liste, 'Vertrauen': vertrauen_liste, 'Angst': furcht_liste, 'Überraschung': überraschung_liste, 'Traurigkeit': traurigkeit_liste, 'Ekel': ekel_liste, 'Ärger': zorn_liste, 'Erwartung': erwartung_liste }


        return EI, cc, CountOhneSTP, faktor, emo_dict

    def count_emo(a_dict, descending = True):
        count = 0
        new_dict = {}
        for i in a_dict:
            if isinstance(a_dict[i], list):
                count += len(a_dict[i]) # Count all values
                x = len(a_dict[i])
            new_dict[i] = x
        if descending == True:
            print(".... descending ...")
            new_dict = {k: v for k, v in sorted(new_dict.items(), key=lambda item: item[1], reverse=True)}
        return new_dict









