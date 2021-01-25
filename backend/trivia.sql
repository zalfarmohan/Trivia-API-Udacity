--
-- PostgreSQL database dump
--

-- Dumped from database version 13.1
-- Dumped by pg_dump version 13.1

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: categories; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.categories (
    id integer NOT NULL,
    type text
);


ALTER TABLE public.categories OWNER TO postgres;

--
-- Name: categories_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.categories_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.categories_id_seq OWNER TO postgres;

--
-- Name: categories_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.categories_id_seq OWNED BY public.categories.id;


--
-- Name: questions; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.questions (
    id integer NOT NULL,
    question text,
    answer text,
    difficulty integer,
    category integer
);


ALTER TABLE public.questions OWNER TO postgres;

--
-- Name: questions_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.questions_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.questions_id_seq OWNER TO postgres;

--
-- Name: questions_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.questions_id_seq OWNED BY public.questions.id;


--
-- Name: categories id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.categories ALTER COLUMN id SET DEFAULT nextval('public.categories_id_seq'::regclass);


--
-- Name: questions id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.questions ALTER COLUMN id SET DEFAULT nextval('public.questions_id_seq'::regclass);


--
-- Data for Name: categories; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.categories (id, type) FROM stdin;
1	Science
2	Art
3	Geography
4	History
5	Entertainment
6	Sports
7	Technology
\.


--
-- Data for Name: questions; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.questions (id, question, answer, difficulty, category) FROM stdin;
2	What movie earned Tom Hanks his third straight Oscar nomination, in 1996?	Apollo 13	4	5
96	Who was the 1st president of BCCI ( Board of Control for Cricket in India )?	R.E. Grant Govan	1	6
97	What is the name of person which controls a football match	Referee	2	6
13	What is the largest lake in Africa?	Lake Victoria	2	3
14	In which royal palace would you find the Hall of Mirrors?	The Palace of Versailles	3	3
15	The Taj Mahal is located in which Indian city?	Agra	2	3
98	 In football, which team has won the Champions League (formerly the European Cup) the most?	Real Madrid (13)	4	6
17	La Giaconda is better known as what?	Mona Lisa	3	2
18	How many paintings did Van Gogh sell in his lifetime?	One	4	2
19	Which American artist was a pioneer of Abstract Expressionism, and a leading exponent of action painting?	Jackson Pollock	2	2
20	What is the heaviest organ in the human body?	The Liver	4	1
21	Who discovered penicillin?	Alexander Fleming	3	1
22	Hematology is a branch of medicine involving the study of what?	Blood	4	1
23	Which dung beetle was worshipped by the ancient Egyptians?	Scarab	4	4
99	 How many players are there in a rugby league team?	13	4	6
100	\t Brass gets discoloured in air because of the presence of which of the following gases in air?	Hydrogen sulphide	1	1
101	Which of the following is a non metal that remains liquid at room temperature?	Bromine	1	1
102	Water is a good solvent of ionic salts because	it has a high dipole moment	5	1
103	Which of the following is the lightest metal?	Lithium	4	1
104	\t In which decade was the American Institute of Electrical Engineers (AIEE) founded?	1880s	3	7
105	What is part of a database that holds only one type of information?	Field	1	7
106	Sometimes computers and cache registers in a foodmart are connected to a UPS system. What does UPS mean?	Uninterruptable Power Supply	5	7
107	What do we call a collection of two or more computers that are located within a limited distance of each other and that are connected to each other directly or indirectly?	Local Area Network	5	7
108	In what year was the "@" chosen for its use in e-mail addresses?	1972	4	7
110	What will a UPS be used for in a building?	To provide power to essential equipment	3	7
\.


--
-- Name: categories_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.categories_id_seq', 6, true);


--
-- Name: questions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.questions_id_seq', 110, true);


--
-- Name: categories categories_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.categories
    ADD CONSTRAINT categories_pkey PRIMARY KEY (id);


--
-- Name: questions questions_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.questions
    ADD CONSTRAINT questions_pkey PRIMARY KEY (id);


--
-- Name: questions category; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.questions
    ADD CONSTRAINT category FOREIGN KEY (category) REFERENCES public.categories(id) ON UPDATE CASCADE ON DELETE SET NULL;


--
-- PostgreSQL database dump complete
--

