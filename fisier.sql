--
-- PostgreSQL database dump
--

\restrict 6hG88ejw60456lW4lork7YR9Uhh6m94QMqba665qRib2t2i1Fe3dvVrJEDlAZcV

-- Dumped from database version 18.6
-- Dumped by pg_dump version 18.6

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET transaction_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- Data for Name: aplicatiehardware_componenta; Type: TABLE DATA; Schema: django; Owner: maxim
--

INSERT INTO django.aplicatiehardware_componenta (id, nume, pret, in_stoc, data_aparitie, data_adaugare, stare, porturi_interfata, brand_id, categorie_id) VALUES (1, 'Arduino Uno Rev3', 120, true, NULL, '2026-10-21 20:20:33.439044+03', 'nou', '{}', 1, 5);
INSERT INTO django.aplicatiehardware_componenta (id, nume, pret, in_stoc, data_aparitie, data_adaugare, stare, porturi_interfata, brand_id, categorie_id) VALUES (2, 'ESP32-WROOM', 35, true, NULL, '2026-10-21 20:20:58.835505+03', 'nou', '{}', 3, 5);
INSERT INTO django.aplicatiehardware_componenta (id, nume, pret, in_stoc, data_aparitie, data_adaugare, stare, porturi_interfata, brand_id, categorie_id) VALUES (3, 'Raspberry Pi 4', 350, true, NULL, '2026-10-21 20:21:19.551776+03', 'nou', '{}', 4, 1);
INSERT INTO django.aplicatiehardware_componenta (id, nume, pret, in_stoc, data_aparitie, data_adaugare, stare, porturi_interfata, brand_id, categorie_id) VALUES (4, 'Senzor Ultrasunete HC-SR04', 15, true, NULL, '2026-10-21 20:21:55.760841+03', 'nou', '{}', 4, 2);
INSERT INTO django.aplicatiehardware_componenta (id, nume, pret, in_stoc, data_aparitie, data_adaugare, stare, porturi_interfata, brand_id, categorie_id) VALUES (5, 'Servomotor SG90', 20, true, NULL, '2026-10-21 20:22:20.039373+03', 'nou', '{}', 5, 4);
INSERT INTO django.aplicatiehardware_componenta (id, nume, pret, in_stoc, data_aparitie, data_adaugare, stare, porturi_interfata, brand_id, categorie_id) VALUES (6, 'Senzor Temperatura DHT11', 18, true, NULL, '2026-10-21 20:22:41.428572+03', 'nou', '{}', 4, 4);
INSERT INTO django.aplicatiehardware_componenta (id, nume, pret, in_stoc, data_aparitie, data_adaugare, stare, porturi_interfata, brand_id, categorie_id) VALUES (7, 'Acumulator Li-Po 1000mAh', 45, true, NULL, '2026-10-21 20:23:07.780616+03', 'nou', '{}', 3, 5);
INSERT INTO django.aplicatiehardware_componenta (id, nume, pret, in_stoc, data_aparitie, data_adaugare, stare, porturi_interfata, brand_id, categorie_id) VALUES (8, 'Modul Bluetooth HC-05', 25, true, NULL, '2026-10-21 20:23:28.27167+03', 'nou', '{}', 2, 1);
INSERT INTO django.aplicatiehardware_componenta (id, nume, pret, in_stoc, data_aparitie, data_adaugare, stare, porturi_interfata, brand_id, categorie_id) VALUES (9, 'Arduino Mega 2560', 120, true, NULL, '2026-10-21 20:24:09.175005+03', 'nou', '{}', 1, 2);
INSERT INTO django.aplicatiehardware_componenta (id, nume, pret, in_stoc, data_aparitie, data_adaugare, stare, porturi_interfata, brand_id, categorie_id) VALUES (10, 'Releu 5V 1 Canal', 12, true, NULL, '2026-10-21 20:24:30.406698+03', 'nou', '{}', 5, 3);


--
-- Name: aplicatiehardware_componenta_id_seq; Type: SEQUENCE SET; Schema: django; Owner: maxim
--

SELECT pg_catalog.setval('django.aplicatiehardware_componenta_id_seq', 10, true);


--
-- PostgreSQL database dump complete
--

\unrestrict 6hG88ejw60456lW4lork7YR9Uhh6m94QMqba665qRib2t2i1Fe3dvVrJEDlAZcV

--
-- PostgreSQL database dump
--

\restrict ApiQZioraavEFawrEd2KbA6eHcVobdSTbEbA3gA8VrOxpzVEcJLq8OFggqIdcwu

-- Dumped from database version 18.6
-- Dumped by pg_dump version 18.6

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET transaction_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- Data for Name: aplicatiehardware_categorie; Type: TABLE DATA; Schema: django; Owner: maxim
--

INSERT INTO django.aplicatiehardware_categorie (id, nume, descriere, culoare_stilizare, sigla, nivel_dificultate) VALUES (1, 'Microcontrolere', '', '#FFFFFF', '', 'mediu');
INSERT INTO django.aplicatiehardware_categorie (id, nume, descriere, culoare_stilizare, sigla, nivel_dificultate) VALUES (2, 'Senzori', '', '#FFFFFF', '', 'mediu');
INSERT INTO django.aplicatiehardware_categorie (id, nume, descriere, culoare_stilizare, sigla, nivel_dificultate) VALUES (3, 'Actuatoare', '', '#FFFFFF', '', 'mediu');
INSERT INTO django.aplicatiehardware_categorie (id, nume, descriere, culoare_stilizare, sigla, nivel_dificultate) VALUES (4, 'Conectivitate', '', '#FFFFFF', '', 'mediu');
INSERT INTO django.aplicatiehardware_categorie (id, nume, descriere, culoare_stilizare, sigla, nivel_dificultate) VALUES (5, 'Alimentare', '', '#FFFFFF', '', 'mediu');


--
-- Name: aplicatiehardware_categorie_id_seq; Type: SEQUENCE SET; Schema: django; Owner: maxim
--

SELECT pg_catalog.setval('django.aplicatiehardware_categorie_id_seq', 5, true);


--
-- PostgreSQL database dump complete
--

\unrestrict ApiQZioraavEFawrEd2KbA6eHcVobdSTbEbA3gA8VrOxpzVEcJLq8OFggqIdcwu

--
-- PostgreSQL database dump
--

\restrict 3qmqLWB5y1ubKfFBEukx3NwXazJTmjVnnLfN4a8FWAfuLfodoGrOo9jzrMVnPWZ

-- Dumped from database version 18.6
-- Dumped by pg_dump version 18.6

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET transaction_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- Data for Name: aplicatiehardware_brand; Type: TABLE DATA; Schema: django; Owner: maxim
--

INSERT INTO django.aplicatiehardware_brand (id, nume, tara_origine, website) VALUES (1, 'Arduino', 'Italia', 'https://www.arduino.cc');
INSERT INTO django.aplicatiehardware_brand (id, nume, tara_origine, website) VALUES (2, 'Raspberry Pi', 'Marea Britanie', 'https://www.raspberrypi.org');
INSERT INTO django.aplicatiehardware_brand (id, nume, tara_origine, website) VALUES (3, 'Espressif', 'China', 'https://www.espressif.com');
INSERT INTO django.aplicatiehardware_brand (id, nume, tara_origine, website) VALUES (4, 'Adafruit', 'SUA', 'https://www.adafruit.com');
INSERT INTO django.aplicatiehardware_brand (id, nume, tara_origine, website) VALUES (5, 'SparkFun', 'SUA', 'https://www.sparkfun.com');


--
-- Name: aplicatiehardware_brand_id_seq; Type: SEQUENCE SET; Schema: django; Owner: maxim
--

SELECT pg_catalog.setval('django.aplicatiehardware_brand_id_seq', 5, true);


--
-- PostgreSQL database dump complete
--

\unrestrict 3qmqLWB5y1ubKfFBEukx3NwXazJTmjVnnLfN4a8FWAfuLfodoGrOo9jzrMVnPWZ

--
-- PostgreSQL database dump
--

\restrict SWsrmlh2b0kfC3BkIm8MIBmLe3E0GYQaARk6fvCa2U6u3g2SpFTISoF7lEvmqvf

-- Dumped from database version 18.6
-- Dumped by pg_dump version 18.6

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET transaction_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- Data for Name: aplicatiehardware_furnizor; Type: TABLE DATA; Schema: django; Owner: maxim
--

INSERT INTO django.aplicatiehardware_furnizor (id, nume_companie, email_contact, telefon) VALUES (1, 'RoboFun', 'vanzari@robofun.ro', '0712345678');
INSERT INTO django.aplicatiehardware_furnizor (id, nume_companie, email_contact, telefon) VALUES (2, 'Optimus Digital', 'contact@optimus.ro', '0723456789');
INSERT INTO django.aplicatiehardware_furnizor (id, nume_companie, email_contact, telefon) VALUES (3, 'Clește', 'salut@cleste.ro', '0734567890');
INSERT INTO django.aplicatiehardware_furnizor (id, nume_companie, email_contact, telefon) VALUES (4, 'Farnell', 'comenzi@farnell.ro', '0745678901');
INSERT INTO django.aplicatiehardware_furnizor (id, nume_companie, email_contact, telefon) VALUES (5, 'Mouser', 'sales@mouser.com', '0756789012');


--
-- Name: aplicatiehardware_furnizor_id_seq; Type: SEQUENCE SET; Schema: django; Owner: maxim
--

SELECT pg_catalog.setval('django.aplicatiehardware_furnizor_id_seq', 5, true);


--
-- PostgreSQL database dump complete
--

\unrestrict SWsrmlh2b0kfC3BkIm8MIBmLe3E0GYQaARk6fvCa2U6u3g2SpFTISoF7lEvmqvf

--
-- PostgreSQL database dump
--

\restrict kyTBrOE8a2BrQmS3z1nqsOBr3SuV9Y0LhGYoK4XHASflsX1iCQJDq3kNoTjFX0j

-- Dumped from database version 18.6
-- Dumped by pg_dump version 18.6

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET transaction_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- Data for Name: aplicatiehardware_specificatietehnica; Type: TABLE DATA; Schema: django; Owner: maxim
--

INSERT INTO django.aplicatiehardware_specificatietehnica (id, nume_spec, valoare, componenta_id) VALUES (1, 'Pini I/O', '14', 1);
INSERT INTO django.aplicatiehardware_specificatietehnica (id, nume_spec, valoare, componenta_id) VALUES (2, 'Tensiune alimentare', '3.3V', 2);
INSERT INTO django.aplicatiehardware_specificatietehnica (id, nume_spec, valoare, componenta_id) VALUES (3, 'Memorie RAM', '4GB', 3);
INSERT INTO django.aplicatiehardware_specificatietehnica (id, nume_spec, valoare, componenta_id) VALUES (4, 'Distanta maxima', '400cm', 4);
INSERT INTO django.aplicatiehardware_specificatietehnica (id, nume_spec, valoare, componenta_id) VALUES (5, 'Cuplu', '1.8kg-cm', 5);


--
-- Name: aplicatiehardware_specificatietehnica_id_seq; Type: SEQUENCE SET; Schema: django; Owner: maxim
--

SELECT pg_catalog.setval('django.aplicatiehardware_specificatietehnica_id_seq', 5, true);


--
-- PostgreSQL database dump complete
--

\unrestrict kyTBrOE8a2BrQmS3z1nqsOBr3SuV9Y0LhGYoK4XHASflsX1iCQJDq3kNoTjFX0j

