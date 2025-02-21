-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Хост: 127.0.0.1:3306
-- Время создания: Фев 22 2025 г., 00:34
-- Версия сервера: 8.0.30
-- Версия PHP: 7.2.34

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- База данных: `sewing_factory`
--

-- --------------------------------------------------------

--
-- Структура таблицы `customer`
--

CREATE TABLE `customer` (
  `id` int NOT NULL,
  `company_name` varchar(255) NOT NULL,
  `surname` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `patronymic` varchar(255) NOT NULL,
  `login` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL,
  `phone` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  `id_type_customer` int DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Дамп данных таблицы `customer`
--

INSERT INTO `customer` (`id`, `company_name`, `surname`, `name`, `patronymic`, `login`, `password`, `phone`, `email`, `id_type_customer`) VALUES
(1, 'ООО МодаСтиль', 'Петров', 'Алексей', 'Игоревич', 'client1', 'pass123', '+79165554433', 'client1@mail.ru', 1),
(2, '', 'Соколова', 'Мария', 'Дмитриевна', 'client2', 'pass456', '+79036667788', 'client2@yandex.ru', 2),
(3, 'ООО СтильПлюс', 'Иванова', 'Елена', 'Владимировна', 'client3', 'pass789', '+79169998877', 'client3@gmail.com', 1),
(4, '', 'Новиков', 'Павел', 'Сергеевич', 'client4', 'pass000', '+79031112233', 'client4@mail.ru', 2);

-- --------------------------------------------------------

--
-- Структура таблицы `making_product_log`
--

CREATE TABLE `making_product_log` (
  `id` int NOT NULL,
  `product_id` int DEFAULT NULL,
  `old_stage_id` int DEFAULT NULL,
  `new_stage_id` int DEFAULT NULL,
  `timestamp` timestamp NULL DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Структура таблицы `making_product_stage`
--

CREATE TABLE `making_product_stage` (
  `id` int NOT NULL,
  `name` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Дамп данных таблицы `making_product_stage`
--

INSERT INTO `making_product_stage` (`id`, `name`) VALUES
(1, 'Раскрой'),
(2, 'Пришивание фурнитуры');

-- --------------------------------------------------------

--
-- Структура таблицы `material`
--

CREATE TABLE `material` (
  `id` int NOT NULL,
  `id_category` int NOT NULL,
  `id_type` int NOT NULL,
  `name` varchar(255) NOT NULL,
  `color` varchar(255) NOT NULL,
  `photo` blob NOT NULL,
  `quantity` int NOT NULL,
  `density` decimal(10,2) NOT NULL,
  `structure` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Дамп данных таблицы `material`
--

INSERT INTO `material` (`id`, `id_category`, `id_type`, `name`, `color`, `photo`, `quantity`, `density`, `structure`) VALUES
(1, 1, 1, 'Хлопковая ткань', 'белый', '', 100, '150.00', 'плетение 1x1'),
(2, 1, 2, 'Полиэстеровая ткань', 'синий', '', 80, '120.00', 'саржевое плетение'),
(3, 2, 3, 'Нитки шелковые', 'черный', '', 200, '50.00', 'крученые'),
(4, 4, 4, 'Льняная ткань', 'бежевый', '', 75, '180.00', 'полотняное плетение'),
(5, 5, 5, 'Стразы', 'прозрачный', '', 500, '10.00', 'круглые 5мм');

-- --------------------------------------------------------

--
-- Структура таблицы `material_category`
--

CREATE TABLE `material_category` (
  `id` int NOT NULL,
  `name` varchar(255) NOT NULL,
  `accounting_unit` varchar(255) NOT NULL,
  `unit_of_measure` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Дамп данных таблицы `material_category`
--

INSERT INTO `material_category` (`id`, `name`, `accounting_unit`, `unit_of_measure`) VALUES
(1, 'Ткань', 'метр', 'м²'),
(2, 'Нитки', 'катушка', 'шт'),
(3, 'Фурнитура', 'штука', 'шт'),
(4, 'Подкладочные материалы', 'рулон', 'м²'),
(5, 'Декоративные элементы', 'упаковка', 'шт');

-- --------------------------------------------------------

--
-- Структура таблицы `material_request`
--

CREATE TABLE `material_request` (
  `id` int NOT NULL,
  `id_material` int NOT NULL,
  `quantity` int NOT NULL,
  `id_manager` int NOT NULL,
  `id_supplier` int NOT NULL,
  `request_date` datetime NOT NULL,
  `id_status` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Структура таблицы `material_supply`
--

CREATE TABLE `material_supply` (
  `id` int NOT NULL,
  `id_material` int NOT NULL,
  `id_supply` int NOT NULL,
  `purchase_price` decimal(10,2) NOT NULL,
  `width` decimal(10,2) NOT NULL,
  `length` decimal(10,2) NOT NULL,
  `number_accounting_units` int NOT NULL,
  `number_units_measurement` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Дамп данных таблицы `material_supply`
--

INSERT INTO `material_supply` (`id`, `id_material`, `id_supply`, `purchase_price`, `width`, `length`, `number_accounting_units`, `number_units_measurement`) VALUES
(1, 1, 1, '200.00', '1.50', '100.00', 50, 50),
(2, 2, 2, '150.00', '1.20', '80.00', 40, 40),
(3, 4, 3, '300.00', '1.40', '90.00', 30, 30),
(4, 5, 4, '50.00', '0.00', '0.00', 100, 100);

-- --------------------------------------------------------

--
-- Структура таблицы `material_type`
--

CREATE TABLE `material_type` (
  `id` int NOT NULL,
  `name` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Дамп данных таблицы `material_type`
--

INSERT INTO `material_type` (`id`, `name`) VALUES
(1, 'Хлопок'),
(2, 'Полиэстер'),
(3, 'Шелк'),
(4, 'Лен'),
(5, 'Вискоза');

-- --------------------------------------------------------

--
-- Структура таблицы `orders`
--

CREATE TABLE `orders` (
  `id` int NOT NULL,
  `create_date` datetime NOT NULL,
  `number_of_products` int NOT NULL,
  `status_id` int NOT NULL,
  `id_customer` int NOT NULL,
  `id_manager` int NOT NULL,
  `total_cost` decimal(10,2) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Дамп данных таблицы `orders`
--

INSERT INTO `orders` (`id`, `create_date`, `number_of_products`, `status_id`, `id_customer`, `id_manager`, `total_cost`) VALUES
(1, '2023-10-10 09:00:00', 2, 1, 1, 1, '3000.00'),
(2, '2023-10-11 10:00:00', 1, 1, 2, 1, '5000.00'),
(3, '2023-11-10 10:30:00', 3, 1, 3, 1, '24000.00'),
(4, '2023-11-11 11:45:00', 2, 1, 4, 1, '7000.00');

-- --------------------------------------------------------

--
-- Структура таблицы `orders_material`
--

CREATE TABLE `orders_material` (
  `order_id` int DEFAULT NULL,
  `material_id` int DEFAULT NULL,
  `quantity` int DEFAULT NULL,
  `cutting_scheme` varchar(150) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Структура таблицы `orders_storage`
--

CREATE TABLE `orders_storage` (
  `order_id` int NOT NULL,
  `movement_type` varchar(30) NOT NULL,
  `old_location_id` int DEFAULT NULL,
  `new_location_id` int DEFAULT NULL,
  `old_quantity` int NOT NULL,
  `new_quantity` int NOT NULL,
  `timestamp` timestamp NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Структура таблицы `order_status`
--

CREATE TABLE `order_status` (
  `id` int NOT NULL,
  `name` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Дамп данных таблицы `order_status`
--

INSERT INTO `order_status` (`id`, `name`) VALUES
(1, 'Новый'),
(2, 'Ожидает'),
(3, 'Обработка'),
(4, 'Отклонен'),
(5, 'К оплате'),
(6, 'Оплачен'),
(7, 'Раскрой'),
(8, 'Готов');

-- --------------------------------------------------------

--
-- Структура таблицы `order_status_log`
--

CREATE TABLE `order_status_log` (
  `id` int NOT NULL,
  `order_id` int DEFAULT NULL,
  `old_status_id` int DEFAULT NULL,
  `new_status_id` int DEFAULT NULL,
  `timestamp` timestamp NULL DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Структура таблицы `product`
--

CREATE TABLE `product` (
  `id` int NOT NULL,
  `id_order` int NOT NULL,
  `product_type_id` int NOT NULL,
  `height` int NOT NULL,
  `width` int NOT NULL,
  `quantity` int NOT NULL,
  `cost_of_one` decimal(10,2) NOT NULL,
  `making_stage_id` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Дамп данных таблицы `product`
--

INSERT INTO `product` (`id`, `id_order`, `product_type_id`, `height`, `width`, `quantity`, `cost_of_one`, `making_stage_id`) VALUES
(1, 1, 1, 0, 0, 2, '3000.00', 1),
(2, 2, 2, 0, 0, 1, '5000.00', 1),
(3, 3, 3, 0, 0, 3, '24000.00', 1),
(4, 4, 4, 0, 0, 2, '7000.00', 1);

-- --------------------------------------------------------

--
-- Структура таблицы `product_material`
--

CREATE TABLE `product_material` (
  `id` int NOT NULL,
  `id_product` int NOT NULL,
  `id_material` int NOT NULL,
  `quantity` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Дамп данных таблицы `product_material`
--

INSERT INTO `product_material` (`id`, `id_product`, `id_material`, `quantity`) VALUES
(1, 1, 1, 2),
(2, 1, 3, 1),
(3, 2, 2, 3),
(4, 2, 3, 2),
(5, 3, 1, 3),
(6, 3, 4, 2),
(7, 4, 2, 1),
(8, 4, 5, 50);

-- --------------------------------------------------------

--
-- Структура таблицы `product_type`
--

CREATE TABLE `product_type` (
  `id` int NOT NULL,
  `name` varchar(255) NOT NULL,
  `description` text NOT NULL,
  `usage_information` text CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `photo` blob NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Дамп данных таблицы `product_type`
--

INSERT INTO `product_type` (`id`, `name`, `description`, `usage_information`, `photo`) VALUES
(1, 'полотенца', 'Хлопковая ', 'Размеры: M, L, XL', ''),
(2, 'салфетки', 'Вечерние', 'Размер: S', ''),
(3, 'скатерть', 'Классическая', 'Размеры: 48-52', ''),
(4, 'скатерть', 'Праздничная', 'Отделка стразами', '');

-- --------------------------------------------------------

--
-- Структура таблицы `request_status`
--

CREATE TABLE `request_status` (
  `id` int NOT NULL,
  `status_name` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Дамп данных таблицы `request_status`
--

INSERT INTO `request_status` (`id`, `status_name`) VALUES
(1, 'Новая'),
(2, 'Принята'),
(3, 'Отклонена');

-- --------------------------------------------------------

--
-- Структура таблицы `role`
--

CREATE TABLE `role` (
  `id` int NOT NULL,
  `role_name` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Дамп данных таблицы `role`
--

INSERT INTO `role` (`id`, `role_name`) VALUES
(1, 'Менеджер'),
(2, 'Директор'),
(3, 'Кладовщик');

-- --------------------------------------------------------

--
-- Структура таблицы `storage_location`
--

CREATE TABLE `storage_location` (
  `id` int NOT NULL,
  `shelf_number` int NOT NULL,
  `row_number` int NOT NULL,
  `place_number` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Дамп данных таблицы `storage_location`
--

INSERT INTO `storage_location` (`id`, `shelf_number`, `row_number`, `place_number`) VALUES
(1, 1, 1, 1),
(2, 1, 1, 2),
(3, 2, 1, 1),
(4, 2, 2, 1),
(5, 3, 1, 1),
(6, 3, 2, 2),
(7, 4, 1, 1);

-- --------------------------------------------------------

--
-- Структура таблицы `supplier`
--

CREATE TABLE `supplier` (
  `id` int NOT NULL,
  `company_name` varchar(255) NOT NULL,
  `contact_surname` varchar(255) NOT NULL,
  `contact_name` varchar(255) NOT NULL,
  `phone` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  `city` varchar(255) NOT NULL,
  `street` varchar(255) NOT NULL,
  `house` varchar(255) NOT NULL,
  `INN` varchar(255) NOT NULL,
  `bic` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Дамп данных таблицы `supplier`
--

INSERT INTO `supplier` (`id`, `company_name`, `contact_surname`, `contact_name`, `phone`, `email`, `city`, `street`, `house`, `INN`, `bic`) VALUES
(1, 'ООО ТекстильПро', 'Иванов', 'Петр', '+79161234567', 'textilepro@mail.ru', 'Москва', 'Ленина', '10', '1234567890', '044525201'),
(2, 'ЗАО Ниточка', 'Смирнова', 'Ольга', '+79031234567', 'nitochka@yandex.ru', 'Санкт-Петербург', 'Пушкина', '5', '0987654321', '044525202'),
(3, 'ООО ДекоТекс', 'Сидоров', 'Андрей', '+79167776655', 'dekotex@mail.ru', 'Казань', 'Советская', '15', '1122334455', '044525203'),
(4, 'ИП Кротов', 'Кротов', 'Максим', '+79035554433', 'krotov@yandex.ru', 'Новосибирск', 'Мира', '7', '9988776655', '044525204');

-- --------------------------------------------------------

--
-- Структура таблицы `supply`
--

CREATE TABLE `supply` (
  `id` int NOT NULL,
  `id_supplier` int NOT NULL,
  `data` date NOT NULL,
  `total_cost` decimal(10,2) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Дамп данных таблицы `supply`
--

INSERT INTO `supply` (`id`, `id_supplier`, `data`, `total_cost`) VALUES
(1, 1, '2023-10-01', '50000.00'),
(2, 2, '2023-10-05', '30000.00'),
(3, 3, '2023-11-01', '45000.00'),
(4, 4, '2023-11-05', '25000.00');

-- --------------------------------------------------------

--
-- Структура таблицы `type_customer`
--

CREATE TABLE `type_customer` (
  `id` int NOT NULL,
  `name_type_customer` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Дамп данных таблицы `type_customer`
--

INSERT INTO `type_customer` (`id`, `name_type_customer`) VALUES
(1, 'Юридическое лицо'),
(2, 'Физическое лицо');

-- --------------------------------------------------------

--
-- Структура таблицы `warehouse_movement`
--

CREATE TABLE `warehouse_movement` (
  `id` int NOT NULL,
  `id_material_supply` int NOT NULL,
  `type_movement` varchar(255) NOT NULL,
  `id_old_location` int NOT NULL,
  `id_new_location` int NOT NULL,
  `old_quantity` int NOT NULL,
  `new_quantity` int NOT NULL,
  `data_time` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Дамп данных таблицы `warehouse_movement`
--

INSERT INTO `warehouse_movement` (`id`, `id_material_supply`, `type_movement`, `id_old_location`, `id_new_location`, `old_quantity`, `new_quantity`, `data_time`) VALUES
(1, 1, 'Поступление', 1, 2, 0, 50, '2023-10-01 12:00:00'),
(2, 2, 'Поступление', 3, 4, 0, 40, '2023-10-05 14:00:00'),
(3, 3, 'Поступление', 5, 6, 0, 30, '2023-11-01 15:00:00'),
(4, 4, 'Поступление', 7, 5, 0, 100, '2023-11-05 16:30:00');

-- --------------------------------------------------------

--
-- Структура таблицы `worker`
--

CREATE TABLE `worker` (
  `id` int NOT NULL,
  `surname` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `patronymic` varchar(255) NOT NULL,
  `login` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL,
  `phone` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  `id_role` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Дамп данных таблицы `worker`
--

INSERT INTO `worker` (`id`, `surname`, `name`, `patronymic`, `login`, `password`, `phone`, `email`, `id_role`) VALUES
(1, 'Кузнецов', 'Дмитрий', 'Сергеевич', 'manager1', 'managerpass', '+79167778899', 'manager@mail.ru', 1),
(2, 'Васильев', 'Иван', 'Петрович', 'storekeeper1', 'storepass', '+79031231212', 'store@mail.ru', 3),
(3, 'Федоров', 'Александр', 'Михайлович', 'worker1', 'workerpass', '+79034445566', 'worker@mail.ru', 3),
(4, 'Григорьева', 'Ольга', 'Ивановна', 'quality1', 'qualitypass', '+79161234567', 'quality@mail.ru', 3);

-- --------------------------------------------------------

--
-- Структура таблицы `write_off`
--

CREATE TABLE `write_off` (
  `id` int NOT NULL,
  `material_id` int NOT NULL,
  `quantity` int NOT NULL,
  `width` decimal(10,1) DEFAULT NULL,
  `length` decimal(10,1) DEFAULT NULL,
  `reason` varchar(255) NOT NULL,
  `timestamp` timestamp NOT NULL,
  `can_be_used` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Дамп данных таблицы `write_off`
--

INSERT INTO `write_off` (`id`, `material_id`, `quantity`, `width`, `length`, `reason`, `timestamp`, `can_be_used`) VALUES
(1, 1, 1, NULL, NULL, 'порча материала', '2025-02-05 19:52:55', 0),
(2, 1, 1, NULL, NULL, 'перерасход', '2025-02-04 21:00:00', 0),
(3, 1, 3, '1.5', '0.3', 'перерасход ткани', '2025-01-08 21:00:00', 0),
(4, 1, 5, NULL, NULL, 'брак страз', '2025-01-08 21:00:00', 0),
(5, 2, 1, '1.5', '5.5', 'часть рулона ушла на производство', '2025-02-21 21:03:08', 1);

--
-- Индексы сохранённых таблиц
--

--
-- Индексы таблицы `customer`
--
ALTER TABLE `customer`
  ADD PRIMARY KEY (`id`),
  ADD KEY `id_type_customer` (`id_type_customer`);

--
-- Индексы таблицы `making_product_log`
--
ALTER TABLE `making_product_log`
  ADD PRIMARY KEY (`id`),
  ADD KEY `old_stage_id` (`old_stage_id`),
  ADD KEY `new_stage_id` (`new_stage_id`),
  ADD KEY `product_id` (`product_id`);

--
-- Индексы таблицы `making_product_stage`
--
ALTER TABLE `making_product_stage`
  ADD PRIMARY KEY (`id`);

--
-- Индексы таблицы `material`
--
ALTER TABLE `material`
  ADD PRIMARY KEY (`id`),
  ADD KEY `id_category` (`id_category`,`id_type`),
  ADD KEY `id_type` (`id_type`);

--
-- Индексы таблицы `material_category`
--
ALTER TABLE `material_category`
  ADD PRIMARY KEY (`id`);

--
-- Индексы таблицы `material_request`
--
ALTER TABLE `material_request`
  ADD PRIMARY KEY (`id`),
  ADD KEY `id_material` (`id_material`),
  ADD KEY `id_manager` (`id_manager`),
  ADD KEY `id_supplier` (`id_supplier`),
  ADD KEY `id_status` (`id_status`);

--
-- Индексы таблицы `material_supply`
--
ALTER TABLE `material_supply`
  ADD PRIMARY KEY (`id`),
  ADD KEY `id_material` (`id_material`,`id_supply`),
  ADD KEY `id_supply` (`id_supply`);

--
-- Индексы таблицы `material_type`
--
ALTER TABLE `material_type`
  ADD PRIMARY KEY (`id`);

--
-- Индексы таблицы `orders`
--
ALTER TABLE `orders`
  ADD PRIMARY KEY (`id`),
  ADD KEY `id_customer` (`id_customer`,`id_manager`),
  ADD KEY `id_manager` (`id_manager`),
  ADD KEY `status_id` (`status_id`);

--
-- Индексы таблицы `orders_material`
--
ALTER TABLE `orders_material`
  ADD KEY `order_id` (`order_id`),
  ADD KEY `material_id` (`material_id`);

--
-- Индексы таблицы `orders_storage`
--
ALTER TABLE `orders_storage`
  ADD KEY `order_id` (`order_id`),
  ADD KEY `old_location_id` (`old_location_id`),
  ADD KEY `new_location_id` (`new_location_id`);

--
-- Индексы таблицы `order_status`
--
ALTER TABLE `order_status`
  ADD PRIMARY KEY (`id`);

--
-- Индексы таблицы `order_status_log`
--
ALTER TABLE `order_status_log`
  ADD PRIMARY KEY (`id`),
  ADD KEY `old_status_id` (`old_status_id`),
  ADD KEY `new_status_id` (`new_status_id`),
  ADD KEY `order_id` (`order_id`);

--
-- Индексы таблицы `product`
--
ALTER TABLE `product`
  ADD PRIMARY KEY (`id`),
  ADD KEY `id_order` (`id_order`,`product_type_id`),
  ADD KEY `id_product` (`product_type_id`),
  ADD KEY `making_stage_id` (`making_stage_id`);

--
-- Индексы таблицы `product_material`
--
ALTER TABLE `product_material`
  ADD PRIMARY KEY (`id`),
  ADD KEY `id_product` (`id_product`,`id_material`),
  ADD KEY `id_material` (`id_material`);

--
-- Индексы таблицы `product_type`
--
ALTER TABLE `product_type`
  ADD PRIMARY KEY (`id`);

--
-- Индексы таблицы `request_status`
--
ALTER TABLE `request_status`
  ADD PRIMARY KEY (`id`);

--
-- Индексы таблицы `role`
--
ALTER TABLE `role`
  ADD PRIMARY KEY (`id`);

--
-- Индексы таблицы `storage_location`
--
ALTER TABLE `storage_location`
  ADD PRIMARY KEY (`id`);

--
-- Индексы таблицы `supplier`
--
ALTER TABLE `supplier`
  ADD PRIMARY KEY (`id`);

--
-- Индексы таблицы `supply`
--
ALTER TABLE `supply`
  ADD PRIMARY KEY (`id`),
  ADD KEY `id_supplier` (`id_supplier`);

--
-- Индексы таблицы `type_customer`
--
ALTER TABLE `type_customer`
  ADD PRIMARY KEY (`id`);

--
-- Индексы таблицы `warehouse_movement`
--
ALTER TABLE `warehouse_movement`
  ADD PRIMARY KEY (`id`),
  ADD KEY `id_material_supply` (`id_material_supply`,`id_old_location`,`id_new_location`),
  ADD KEY `id_old_location` (`id_old_location`,`id_new_location`),
  ADD KEY `id_new_location` (`id_new_location`);

--
-- Индексы таблицы `worker`
--
ALTER TABLE `worker`
  ADD PRIMARY KEY (`id`),
  ADD KEY `id_role` (`id_role`);

--
-- Индексы таблицы `write_off`
--
ALTER TABLE `write_off`
  ADD PRIMARY KEY (`id`),
  ADD KEY `material_id` (`material_id`);

--
-- AUTO_INCREMENT для сохранённых таблиц
--

--
-- AUTO_INCREMENT для таблицы `customer`
--
ALTER TABLE `customer`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT для таблицы `making_product_log`
--
ALTER TABLE `making_product_log`
  MODIFY `id` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT для таблицы `making_product_stage`
--
ALTER TABLE `making_product_stage`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT для таблицы `material`
--
ALTER TABLE `material`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT для таблицы `material_category`
--
ALTER TABLE `material_category`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT для таблицы `material_request`
--
ALTER TABLE `material_request`
  MODIFY `id` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT для таблицы `material_supply`
--
ALTER TABLE `material_supply`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT для таблицы `material_type`
--
ALTER TABLE `material_type`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT для таблицы `orders`
--
ALTER TABLE `orders`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT для таблицы `order_status`
--
ALTER TABLE `order_status`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT для таблицы `order_status_log`
--
ALTER TABLE `order_status_log`
  MODIFY `id` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT для таблицы `product`
--
ALTER TABLE `product`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT для таблицы `product_material`
--
ALTER TABLE `product_material`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT для таблицы `product_type`
--
ALTER TABLE `product_type`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT для таблицы `request_status`
--
ALTER TABLE `request_status`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT для таблицы `role`
--
ALTER TABLE `role`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT для таблицы `storage_location`
--
ALTER TABLE `storage_location`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT для таблицы `supplier`
--
ALTER TABLE `supplier`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT для таблицы `supply`
--
ALTER TABLE `supply`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT для таблицы `type_customer`
--
ALTER TABLE `type_customer`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT для таблицы `warehouse_movement`
--
ALTER TABLE `warehouse_movement`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT для таблицы `worker`
--
ALTER TABLE `worker`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT для таблицы `write_off`
--
ALTER TABLE `write_off`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- Ограничения внешнего ключа сохраненных таблиц
--

--
-- Ограничения внешнего ключа таблицы `customer`
--
ALTER TABLE `customer`
  ADD CONSTRAINT `customer_ibfk_1` FOREIGN KEY (`id_type_customer`) REFERENCES `type_customer` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Ограничения внешнего ключа таблицы `making_product_log`
--
ALTER TABLE `making_product_log`
  ADD CONSTRAINT `making_product_log_ibfk_1` FOREIGN KEY (`old_stage_id`) REFERENCES `making_product_stage` (`id`),
  ADD CONSTRAINT `making_product_log_ibfk_2` FOREIGN KEY (`new_stage_id`) REFERENCES `making_product_stage` (`id`),
  ADD CONSTRAINT `making_product_log_ibfk_3` FOREIGN KEY (`product_id`) REFERENCES `product` (`id`);

--
-- Ограничения внешнего ключа таблицы `material`
--
ALTER TABLE `material`
  ADD CONSTRAINT `material_ibfk_1` FOREIGN KEY (`id_category`) REFERENCES `material_category` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `material_ibfk_2` FOREIGN KEY (`id_type`) REFERENCES `material_type` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Ограничения внешнего ключа таблицы `material_request`
--
ALTER TABLE `material_request`
  ADD CONSTRAINT `material_request_ibfk_1` FOREIGN KEY (`id_material`) REFERENCES `material` (`id`),
  ADD CONSTRAINT `material_request_ibfk_2` FOREIGN KEY (`id_manager`) REFERENCES `worker` (`id`),
  ADD CONSTRAINT `material_request_ibfk_3` FOREIGN KEY (`id_supplier`) REFERENCES `supplier` (`id`),
  ADD CONSTRAINT `material_request_ibfk_4` FOREIGN KEY (`id_status`) REFERENCES `request_status` (`id`);

--
-- Ограничения внешнего ключа таблицы `material_supply`
--
ALTER TABLE `material_supply`
  ADD CONSTRAINT `material_supply_ibfk_1` FOREIGN KEY (`id_material`) REFERENCES `material` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `material_supply_ibfk_2` FOREIGN KEY (`id_supply`) REFERENCES `supply` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Ограничения внешнего ключа таблицы `orders`
--
ALTER TABLE `orders`
  ADD CONSTRAINT `orders_ibfk_1` FOREIGN KEY (`id_manager`) REFERENCES `worker` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `orders_ibfk_2` FOREIGN KEY (`id_customer`) REFERENCES `customer` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `orders_ibfk_3` FOREIGN KEY (`status_id`) REFERENCES `order_status` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT;

--
-- Ограничения внешнего ключа таблицы `orders_material`
--
ALTER TABLE `orders_material`
  ADD CONSTRAINT `orders_material_ibfk_1` FOREIGN KEY (`order_id`) REFERENCES `orders` (`id`),
  ADD CONSTRAINT `orders_material_ibfk_2` FOREIGN KEY (`material_id`) REFERENCES `material` (`id`);

--
-- Ограничения внешнего ключа таблицы `orders_storage`
--
ALTER TABLE `orders_storage`
  ADD CONSTRAINT `orders_storage_ibfk_1` FOREIGN KEY (`order_id`) REFERENCES `orders` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  ADD CONSTRAINT `orders_storage_ibfk_2` FOREIGN KEY (`old_location_id`) REFERENCES `storage_location` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  ADD CONSTRAINT `orders_storage_ibfk_3` FOREIGN KEY (`new_location_id`) REFERENCES `storage_location` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT;

--
-- Ограничения внешнего ключа таблицы `order_status_log`
--
ALTER TABLE `order_status_log`
  ADD CONSTRAINT `order_status_log_ibfk_1` FOREIGN KEY (`old_status_id`) REFERENCES `order_status` (`id`),
  ADD CONSTRAINT `order_status_log_ibfk_2` FOREIGN KEY (`new_status_id`) REFERENCES `order_status` (`id`),
  ADD CONSTRAINT `order_status_log_ibfk_3` FOREIGN KEY (`order_id`) REFERENCES `orders` (`id`);

--
-- Ограничения внешнего ключа таблицы `product`
--
ALTER TABLE `product`
  ADD CONSTRAINT `product_ibfk_1` FOREIGN KEY (`id_order`) REFERENCES `orders` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `product_ibfk_2` FOREIGN KEY (`product_type_id`) REFERENCES `product_type` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `product_ibfk_3` FOREIGN KEY (`making_stage_id`) REFERENCES `making_product_stage` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT;

--
-- Ограничения внешнего ключа таблицы `product_material`
--
ALTER TABLE `product_material`
  ADD CONSTRAINT `product_material_ibfk_1` FOREIGN KEY (`id_product`) REFERENCES `product` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `product_material_ibfk_2` FOREIGN KEY (`id_material`) REFERENCES `material` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Ограничения внешнего ключа таблицы `supply`
--
ALTER TABLE `supply`
  ADD CONSTRAINT `supply_ibfk_1` FOREIGN KEY (`id_supplier`) REFERENCES `supplier` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Ограничения внешнего ключа таблицы `warehouse_movement`
--
ALTER TABLE `warehouse_movement`
  ADD CONSTRAINT `warehouse_movement_ibfk_1` FOREIGN KEY (`id_material_supply`) REFERENCES `material_supply` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `warehouse_movement_ibfk_2` FOREIGN KEY (`id_old_location`) REFERENCES `storage_location` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `warehouse_movement_ibfk_3` FOREIGN KEY (`id_new_location`) REFERENCES `storage_location` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Ограничения внешнего ключа таблицы `worker`
--
ALTER TABLE `worker`
  ADD CONSTRAINT `worker_ibfk_1` FOREIGN KEY (`id_role`) REFERENCES `role` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Ограничения внешнего ключа таблицы `write_off`
--
ALTER TABLE `write_off`
  ADD CONSTRAINT `write_off_ibfk_1` FOREIGN KEY (`material_id`) REFERENCES `material` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
